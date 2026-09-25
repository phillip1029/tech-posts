import os,json,urllib.request,urllib.error
p={'model':'typesafe/jev-1.13','state':{'message':'Where is my card?'},'questions':{'intent':{'type':'choice','instructions':'Choose the banking intent.','criteria':{'card_arrival':'card arrival','cash_withdrawal':'cash withdrawal'}}}}
r=urllib.request.Request('https://openrouter.ai/api/alpha/decisions',data=json.dumps(p).encode(),headers={'Authorization':'Bearer '+os.environ['OPENROUTER_API_KEY'],'Content-Type':'application/json'})
try:
 with urllib.request.urlopen(r,timeout=45) as f: result=json.load(f)
except urllib.error.HTTPError as e: result={'status':e.code,'body':e.read().decode()[:1000]}
open('/tmp/jev-benchmark/pilot-result.json','w').write(json.dumps(result,indent=2))
print(json.dumps(result))
