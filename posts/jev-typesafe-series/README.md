# Jev by TypeSafe AI: four-part series

Open [the reading index](index.html). Each article lives in its own folder and uses embedded CSS, with no external fonts or scripts.

1. [Meet Jev](01-what-is-jev/index.html) — 1,677 prose words.
2. [First integration](02-first-jev-api-integration/index.html) — 1,558 prose words.
3. [Confidence and evaluation](03-confidence-and-evaluation/index.html) — 1,783 prose words.
4. [Workflows and costs](04-workflows-and-costs/index.html) — 1,937 prose words.

[Research and editorial notes](research-and-editorial-notes.html) document primary sources, assumptions, and verification boundaries. Sources checked September 25, 2026. Part 4 contains original API measurements on 154 public BANKING77 messages.

The integration article includes editable JSON and Python examples under its `code/` directory. Running the HTTP example requires credentials and can incur charges; reading the articles makes no API requests.

## Visual edition

The original visual edition added process overviews, branch details, primitive and token comparisons, and three interactive examples. Each post retains more than 1,500 prose words. Canonical SVG, source JSON, PNG, and layout reports live in each post’s `assets/` folder; five mobile SVG variants improve phone readability. Shared CSS/JavaScript sources are under the series `assets/` folder and embedded in the HTML.

GIF animation was not generated: the installed Fireworks scene contracts do not support these topologies. The documented dry-run rejection is retained alongside Part 1’s diagrams. Static diagrams and manual controls are the delivered alternatives.

## Public-data benchmark revision

Part 4 now compares Gemini 2.5 Flash-Lite JSON classification with Jev Choice on a fixed 154-message BANKING77 sample. It includes a before/after flow, a static Fireworks process diagram, three Matplotlib charts, and a keyboard-accessible recorded-case explorer. Accuracy: 74.0% versus 80.5%. Known response charges: $0.0174785 versus $0.011034114. One Jev failure has unknown billing and remains included in submitted-message accuracy and timing.

[Benchmark evidence and instructions](04-workflows-and-costs/benchmark/README.md) include all 308 attempts, the pinned dataset manifest, response records, CSV, analysis code, and data license. This small zero-shot sample is not production validation. Older Part 4 conceptual assets remain available for reference; its current figures and controls are embedded in the revised article.
