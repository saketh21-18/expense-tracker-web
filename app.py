from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import os
import sqlite3
from pathlib import Path
from datetime import date

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-only-secret-key-change-in-production')
BASE_DIR = Path(__file__).resolve().parent

# Vercel serverless functions have a temporary writable /tmp directory.
# Keep SQLite in the project database folder locally, but use /tmp on Vercel.
if os.environ.get('VERCEL'):
    DB_PATH = Path('/tmp/expenses.db')
else:
    DB_PATH = BASE_DIR / 'database' / 'expenses.db'

CATEGORIES = ['Food', 'Transport', 'Shopping', 'Bills', 'Education', 'Entertainment', 'Health', 'Other']


def get_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        kind TEXT NOT NULL CHECK(kind IN ('income', 'expense')),
        title TEXT NOT NULL,
        amount REAL NOT NULL CHECK(amount >= 0),
        category TEXT NOT NULL,
        transaction_date TEXT NOT NULL,
        note TEXT DEFAULT ''
    )''')
    conn.commit()
    conn.close()


@app.route('/')
def index():
    conn = get_db()
    transactions = conn.execute('SELECT * FROM transactions ORDER BY transaction_date DESC, id DESC').fetchall()
    stats = conn.execute('''SELECT
        COALESCE(SUM(CASE WHEN kind='income' THEN amount ELSE 0 END),0) income,
        COALESCE(SUM(CASE WHEN kind='expense' THEN amount ELSE 0 END),0) expense,
        COUNT(*) count
        FROM transactions''').fetchone()
    categories = conn.execute('''SELECT category, SUM(amount) total FROM transactions
        WHERE kind='expense' GROUP BY category ORDER BY total DESC''').fetchall()
    conn.close()
    return render_template('index.html', transactions=transactions, stats=stats,
                           categories=categories, categories_list=CATEGORIES, today=date.today().isoformat())


@app.post('/add')
def add_transaction():
    kind = request.form.get('kind', 'expense')
    title = request.form.get('title', '').strip()
    category = request.form.get('category', 'Other')
    transaction_date = request.form.get('transaction_date') or date.today().isoformat()
    note = request.form.get('note', '').strip()
    try:
        amount = float(request.form.get('amount', '0'))
    except ValueError:
        amount = 0
    if kind not in ('income', 'expense') or not title or amount <= 0:
        flash('Please enter valid transaction details.', 'error')
        return redirect(url_for('index'))
    conn = get_db()
    conn.execute('INSERT INTO transactions (kind,title,amount,category,transaction_date,note) VALUES (?,?,?,?,?,?)',
                 (kind, title, amount, category, transaction_date, note))
    conn.commit(); conn.close()
    flash('Transaction added successfully.', 'success')
    return redirect(url_for('index'))


@app.post('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    conn = get_db(); conn.execute('DELETE FROM transactions WHERE id=?', (transaction_id,)); conn.commit(); conn.close()
    flash('Transaction deleted.', 'success')
    return redirect(url_for('index'))


@app.get('/api/summary')
def summary_api():
    conn = get_db()
    rows = conn.execute('''SELECT category, SUM(amount) total FROM transactions
                           WHERE kind='expense' GROUP BY category ORDER BY total DESC''').fetchall()
    conn.close()
    return jsonify({'labels': [r['category'] for r in rows], 'values': [r['total'] for r in rows]})


@app.get('/health')
def health():
    return {'status': 'ok'}


init_db()

if __name__ == '__main__':
    app.run(debug=True)
