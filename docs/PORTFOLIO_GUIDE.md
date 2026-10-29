# Upwork portfolio guide

Use screenshots of the actual demo output plus the code-flow diagrams in `ARCHITECTURE.md`. Do not use generated mockups of applications as if they were real screenshots.

## Suggested items

### 1. Python Job Monitoring — Rule-Based Scoring Demo
- **What to show:** `jobs.py`, the synthetic listing data, a terminal screenshot from `python -m showcase.demo`, and the job-scoring diagram.
- **Claim accurately:** explainable keyword scoring, risk phrase filtering, deterministic ranking, unit tests.
- **Do not claim:** live scraping, AI-based assessment, automatic applications, or real-world performance metrics.

### 2. Context-Aware Chat Assistant — Response Policy Demo
- **What to show:** `chat_policy.py`, the test cases, and the decision flow in `ARCHITECTURE.md`.
- **Claim accurately:** opt-out/quiet-hours/mention gating and deterministic response decisions.
- **Do not claim:** that this mini module is a live Telegram bot or includes an LLM connection.

### 3. AI Video Pipeline — Safe Workflow Planner
- **What to show:** `video_workflow.py`, the ordered steps and the upload approval gate.
- **Claim accurately:** workflow planning, stage separation, and an explicit gate before a publishing step.
- **Do not claim:** this sample generates scripts, voiceovers, renders videos, or uploads content. Those are steps in a plan only.

### 4. SaaS Directory — Typed Domain Logic
- **What to show:** `company_directory.py` and `web/company_directory.ts`.
- **Claim accurately:** typed records, country/sector filtering, deterministic promotional ordering with tie-breaks.
- **Do not claim:** a complete production SaaS backend, authentication, payments, or a deployed ranking service.

### 5. Image Upload Validation — Frontend/Backend Safety Pattern
- **What to show:** `photo_upload.py` and the tests for file type and size.
- **Claim accurately:** basic metadata validation in a small standalone example.
- **Do not claim:** secure file decoding, image enhancement, storage, payment processing, or AI image transformation.

### 6. Market Data — Alert-Only Calculation
- **What to show:** `market_data.py`, sample observations and unit tests.
- **Claim accurately:** a small price-change and relative-volume threshold check on synthetic observations.
- **Do not claim:** price prediction, profitable strategy, backtest results, live data feed, or order execution.

## Screenshot checklist

1. Run the demo locally and capture terminal output.
2. Capture the actual source file in VS Code or GitHub for one short code excerpt per portfolio item.
3. Pair it with the relevant architecture diagram.
4. Hide usernames, local paths, tokens, account IDs, and any private project names.
5. Label all synthetic data and prototypes clearly.
