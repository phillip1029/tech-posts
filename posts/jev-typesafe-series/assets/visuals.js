
(()=>{
 document.querySelectorAll('[data-walkthrough]').forEach(w=>{
  const panels=[...w.querySelectorAll('.step-panel')],controls=w.querySelector('.viz-controls');let index=0;
  controls.hidden=false;
  const draw=()=>{panels.forEach((p,i)=>p.hidden=i!==index);w.querySelector('[data-step-status]').textContent=`Step ${index+1} of ${panels.length}`;w.querySelector('[data-prev]').disabled=index===0;w.querySelector('[data-next]').disabled=index===panels.length-1;};
  w.querySelector('[data-prev]').onclick=()=>{index=Math.max(0,index-1);draw()};w.querySelector('[data-next]').onclick=()=>{index=Math.min(panels.length-1,index+1);draw()};draw();
 });
 const lab=document.querySelector('[data-confidence-lab]');
 if(lab){
  lab.querySelector('.viz-controls').hidden=false;
  const input=lab.querySelector('input');
  const draw=()=>{const t=Number(input.value);let accepted=0,correct=0;lab.querySelector('[data-threshold]').textContent=t.toFixed(2);
   lab.querySelectorAll('tbody tr').forEach(row=>{const accept=row.dataset.choice!=='review'&&Number(row.dataset.confidence)>=t;accepted+=Number(accept);correct+=Number(accept&&row.dataset.choice===row.dataset.reference);const cell=row.querySelector('[data-action]');cell.textContent=accept?'Suggest queue':'Review';cell.className=accept?'outcome-accept':'outcome-review';});
   lab.querySelector('[data-coverage]').textContent=(accepted/8*100).toFixed(1)+'%';lab.querySelector('[data-accuracy]').textContent=accepted?(correct/accepted*100).toFixed(1)+'%':'N/A';lab.querySelector('[data-review]').textContent=String(8-accepted)+' of 8';
  };input.addEventListener('input',draw);draw();
 }
 const calc=document.querySelector('[data-cost-lab]');
 if(calc){
  calc.querySelector('.calc-fields').hidden=false;
  const money=n=>n.toLocaleString('en-US',{style:'currency',currency:'USD',maximumFractionDigits:2});
  const draw=()=>{const fields=[...calc.querySelectorAll('input')];if(fields.some(f=>!f.checkValidity()||f.value==='')){calc.querySelector('[data-cost-status]').textContent='Enter valid non-negative values in every field; review share must be 0–100.';return;}
   const values=Object.fromEntries(fields.map(f=>[f.name,Number(f.value)]));const model=values.requests*values.tokens/1e6*values.price;const hours=values.requests*values.review/100*values.minutes/60;const labor=hours*values.hourly;
   calc.querySelector('[data-model-cost]').textContent=money(model);calc.querySelector('[data-review-cost]').textContent=money(labor);calc.querySelector('[data-subtotal]').textContent=money(model+labor);calc.querySelector('[data-cost-status]').textContent=`Review time: ${hours.toLocaleString('en-US',{maximumFractionDigits:1})} hours. Partial subtotal only; excludes retries, other models, infrastructure and corrections.`;
  };calc.querySelectorAll('input').forEach(f=>f.addEventListener('input',draw));draw();
 }
})();
