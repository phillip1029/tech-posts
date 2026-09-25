"""Recompute tables and figures from recorded responses, without API calls."""
import csv,json,math,statistics
from pathlib import Path
ROOT=Path(__file__).resolve().parent
rows=[json.loads(x) for x in (ROOT/'results.jsonl').read_text().splitlines()]
m=json.loads((ROOT/'manifest.json').read_text()); s=json.loads((ROOT/'summary.json').read_text())
for kind in ['jev','gemini']:
 rr=[r for r in rows if r['kind']==kind];d=s[kind];n=len(rr);p=d['accuracy'];z=1.96
 mid=(p+z*z/(2*n))/(1+z*z/n);radius=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/(1+z*z/n)
 d['wilson95']=[mid-radius,mid+radius]
 good=[r for r in rr if not r['error']];d['valid_accuracy']=sum(r['correct'] for r in good)/len(good)
 d['input_tokens']=sum(r['response']['usage'].get('input_tokens',r['response']['usage'].get('prompt_tokens',0)) for r in good)
 d['output_tokens']=sum(r['response']['usage'].get('output_tokens',r['response']['usage'].get('completion_tokens',0)) for r in good)
 d['max_seconds']=max(r['seconds'] for r in rr)
 d['mean_success_cost']=d['cost_usd']/len(good)
pairs={}
for r in rows:pairs.setdefault(r['row'],{})[r['kind']]=r
b=s['paired']['jev_only'];c=s['paired']['gemini_only'];n=b+c
s['paired']['mcnemar_exact_p']=min(1,2*sum(math.comb(n,k) for k in range(min(b,c)+1))/2**n) if n else 1
(ROOT/'summary.json').write_text(json.dumps(s,indent=2))
fields=['row','text','gold','jev_prediction','gemini_prediction','jev_correct','gemini_correct','jev_seconds','gemini_seconds','jev_cost_usd','gemini_cost_usd','jev_error','gemini_error']
with (ROOT/'comparison.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for item in m['sample']:
  row={k:item[k] for k in ['row','text','gold']}
  for kind in ['jev','gemini']:
   r=pairs[item['row']][kind]
   for key in ['prediction','correct','seconds','error']:row[kind+'_'+key]=r[key]
   row[kind+'_cost_usd']=(r['response'] or {}).get('usage',{}).get('cost')
  w.writerow(row)
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'path'})
asset=ROOT.parent/'assets'
if ROOT.parent.name != '04-workflows-and-costs': asset=asset/'04'
asset.mkdir(parents=True,exist_ok=True)
for name,title,vals,limit,label in [
 ('accuracy','Correct labels on the same 154 messages',[s['gemini']['accuracy']*100,s['jev']['accuracy']*100],100,lambda v:f'{v:.1f}%'),
 ('api-cost','Reported API cost per 1,000 submitted messages',[s['gemini']['cost_per_1000'],s['jev']['cost_per_1000']],None,lambda v:f'${v:.4f}'),
 ('latency','Client elapsed time, including gateway and network',[s['gemini']['median_seconds'],s['jev']['median_seconds']],None,lambda v:f'{v:.3f} s')]:
 fig,ax=plt.subplots(figsize=(8,3.4),layout='constrained');fig.set_facecolor('#fffdf8');ax.set_facecolor('#fffdf8')
 bars=ax.barh(['Without Jev\nGemini Flash-Lite','With Jev\nJev Choice'],vals,color=['#5277a6','#087f80'],height=.45)
 ax.invert_yaxis(); ax.set_xlim(0,limit or max(vals)*1.35);ax.set_title(title,loc='left',fontsize=13,pad=18)
 ax.bar_label(bars,labels=[label(v) for v in vals],padding=8);ax.spines[['top','right','left']].set_visible(False);ax.grid(axis='x',alpha=.18);ax.set_axisbelow(True)
 ax.set_xlabel('Accuracy (%) — failures count as incorrect' if name=='accuracy' else 'USD — successful-response charges; failed-call billing unknown' if name=='api-cost' else 'Seconds — median, one serial run')
 for ext in ['svg','png']:fig.savefig(asset/f'banking77-{name}.{ext}',dpi=160)
 plt.close(fig)
print(json.dumps(s,indent=2))
