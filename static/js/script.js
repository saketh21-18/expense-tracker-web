function openModal(){document.getElementById('modal').classList.add('show')}
function closeModal(){document.getElementById('modal').classList.remove('show')}
window.addEventListener('click',e=>{const m=document.getElementById('modal');if(e.target===m)closeModal()})
function filterTransactions(){const q=document.getElementById('search').value.toLowerCase();document.querySelectorAll('#transactionRows tr').forEach(r=>{r.style.display=r.innerText.toLowerCase().includes(q)?'':'none'})}
if(window.categoryLabels && document.getElementById('expenseChart')){
 new Chart(document.getElementById('expenseChart'),{type:'doughnut',data:{labels:window.categoryLabels,datasets:[{data:window.categoryValues,borderWidth:0}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{position:'right',labels:{usePointStyle:true,padding:15,font:{size:11}}}}}})
}
setTimeout(()=>document.querySelectorAll('.flash').forEach(x=>x.remove()),3200)
