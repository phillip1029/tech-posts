# Jev ticket triage example

Read Part 2 before running. Requires Python 3.10+, network access, and a TypeSafe API key. No third-party Python packages are required.

From this directory, set TYPESAFE_API_KEY in your environment, then run `python3 triage.py`. This sends the fictional message to TypeSafe and may incur API charges. It prints the API response and does not modify a ticket.

`policy.py` contains the separate, offline queue-suggestion function. Its threshold must be supplied by the caller and validated on representative data. It expects a successful, validated Choice answer. It is not a production response validator.

No authenticated API request or model benchmark was performed when preparing this article. The JSON and Python syntax and policy boundary behavior were checked locally.
