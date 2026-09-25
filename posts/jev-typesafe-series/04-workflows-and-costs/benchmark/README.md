# BANKING77: Gemini classifier versus Jev Choice

Original live API measurements collected September 25, 2026 for Part 4. This is a small zero-shot routing benchmark, not a production deployment, latency SLA, or vendor benchmark.

## Files

- `benchmark.py`: Python standard-library sampler, request builder, resumable runner, and offline summary.
- `manifest.json`: pinned dataset revision, SHA-256, seed, category list, selected CSV row numbers, public messages, gold labels, model IDs, and common instruction.
- `results.jsonl`: all 308 attempts, including the failed request; complete successful response bodies, timing, predictions, and correctness. No credentials or request headers.
- `comparison.csv`: 154 paired cases for inspection.
- `summary.json`: aggregate measurements and analysis.
- `analysis.py`: offline CSV and chart builder; requires matplotlib (run used 3.10.9).
- `pilot.py`, `pilot-result.json`: separate synthetic two-option access check. Excluded from benchmark scores and costs; reported charge $0.000013608.
- `DATASET-LICENSE.txt`: upstream CC BY 4.0 license.

Dataset: [BANKING77 by PolyAI](https://github.com/PolyAI-LDN/task-specific-datasets), associated with Casanueva et al., [Efficient Intent Detection with Dual Sentence Encoders](https://arxiv.org/abs/2003.04807). Public messages and labels are reproduced as a sampled CSV/JSON subset under CC BY 4.0. Transformation: sample two rows per category and reorder them; add model predictions and timings. Source content is unmodified.

## Method frozen for the run

Revision `57ec275d8078af65b7731c2a98be812d844a6d6b`; test.csv, 3,080 rows, 77 labels. Seed 20260925, two examples per class, shuffled. Both arms see the same customer text, common classification instruction, and labels described by replacing underscores with spaces. No examples or test gold labels appear in requests. No prompt tuning or confidence threshold.

Jev request model `typesafe/jev-1.13`, returned `typesafe/jev-1.13-20260917`, provider TypeSafe. Gemini requested/returned `google/gemini-2.5-flash-lite`, provider Google. Gemini uses temperature 0, reasoning disabled, max_tokens 64, strict JSON schema enum, require_parameters true and allow_fallbacks false. Jev uses native Choice criteria. Actual tokenization and API wrappers differ. The Gemini model listing announced retirement October 20, 2026; check availability before rerunning.

Serial calls through OpenRouter from one local machine; which model goes first alternates per message. Python urllib client, no explicit persistent connection pool. Timer surrounds request/response reading; no streaming. Both arms have a 45-second request timeout. No application retry. A Jev HTTP 520 at row 2526 paused the first runner; we revised continuation to retain this failure and skip all attempted pairs. No evaluated request was rerun. The pause is visible in timestamps. One earlier synthetic connectivity call is excluded.

## Results and accounting

Jev 124/154 correct (80.5%), Gemini 114/154 (74.0%). Paired counts: 111 both correct, 13 Jev only, 3 Gemini only, 27 both incorrect. Jev has one failed attempt; Gemini has none. Failure counts against submitted-message accuracy. Conditional accuracy on usable responses is separately reported.

Reported API usage charges: Jev $0.011034114 (153 usage-bearing responses), Gemini $0.0174785 (154). Jev failed-call charge is unknown; its total is incomplete and must not be described as an invoice-reconciled cost. Charges per 1,000 submitted = known reported total / 154 * 1,000. Mean cost per usable response uses the successful count. Fees, tax, engineering, infrastructure, retries, correction work, and downstream services are excluded. Total known charges including the separate probe: $0.028526222.

Latency includes all attempts: median is statistics.median; p95 is sorted_times[ceil(.95*n)-1]. Jev median 0.243 s, p95 0.359 s, max 40.150 s; Gemini median 0.617 s, p95 1.058 s, max 1.413 s. This is one serial run, not a concurrency benchmark. No provider-only inference duration is claimed.

`analysis.py` also computes Wilson intervals (simple binomial approximation, not a stratified sampling uncertainty model) and exact two-sided McNemar p-value on discordant pairs. Small sample, two examples per category, possible public-data contamination, and zero-shot prompt design limit generalization. Do not select thresholds or tune prompts on these cases and then continue to call them held out.

## Offline reproduction

Run in this directory; no credentials or network needed:

```sh
python3 benchmark.py
python3 analysis.py
```

The first regenerates basic summary.json; the second adds analysis fields and regenerates comparison.csv and SVG/PNG charts. Matplotlib is needed only for the second. Chart generation uses local paths and makes no inference calls.

## Optional paid live rerun

Create a fresh directory and copy benchmark.py and analysis.py into it. Set `OPENROUTER_API_KEY` through your environment; never place it in saved files or browser code.

```sh
python3 benchmark.py --prepare
python3 benchmark.py --live
python3 analysis.py
```

This downloads the pinned public dataset, sends the 154 sampled messages to both providers, and incurs OpenRouter charges. The $0.50 stop checks *reported* cumulative cost after each successful call; at most one billed call may exceed the threshold, and unknown error charges are not covered. It is not a hard spending cap. Use account-level spending controls if needed. The runner resumes existing logs by skipping attempted pairs, including failures. Start a fresh directory for a new measurement. API availability, pricing, and model versions can change; a rerun is not guaranteed to reproduce stochastic answers or latency.
