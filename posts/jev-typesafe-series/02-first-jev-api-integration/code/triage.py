import json
import os
import urllib.error
import urllib.request

# Save the JSON example as request.json beside this script.
with open("request.json", encoding="utf-8") as source:
    payload = json.load(source)

key = os.environ.get("TYPESAFE_API_KEY")
if not key:
    raise SystemExit("Set TYPESAFE_API_KEY before running this example.")

request = urllib.request.Request(
    "https://api.typesafe.ai/v1/systemone",
    data=json.dumps(payload).encode("utf-8"),
    headers={
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
    },
    method="POST",
)

try:
    with urllib.request.urlopen(request, timeout=30) as reply:
        result = json.load(reply)
except urllib.error.HTTPError as error:
    raise SystemExit(f"HTTP {error.code}; no ticket was changed.") from error
except (urllib.error.URLError, TimeoutError) as error:
    raise SystemExit("Request failed; no ticket was changed.") from error

print(json.dumps(result, indent=2))
