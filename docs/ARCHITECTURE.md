# Architecture notes

These diagrams describe the demonstration modules in this repository, not the full architecture of any private project.

## 1. Job monitoring

```mermaid
flowchart TD
    A[Supplied listing records] --> B[Normalize text]
    B --> C[Risk phrase filter]
    C -->|Risk phrase found| D[Reject with reason]
    C -->|No risk phrase| E[Match target skills]
    E --> F[Bounded rule-based score]
    F --> G[Ranked results for manual review]
```

Files: `src/showcase/jobs.py`, `tests/test_jobs.py`.

## 2. Group assistant decision

```mermaid
flowchart TD
    A[Incoming message event] --> B{Group enabled?}
    B -->|No| X[Do not respond]
    B -->|Yes| C{User opted out?}
    C -->|Yes| X
    C -->|No| D{Quiet hours?}
    D -->|Yes| E{Admin command?}
    E -->|No| X
    E -->|Yes| F[Handle admin command]
    D -->|No| G{Mention or reply to bot?}
    G -->|Yes| H[Respond decision]
    G -->|No| X
```

File: `src/showcase/chat_policy.py`. The module does not send Telegram messages.

## 3. Video pipeline planner

```mermaid
flowchart TD
    A[Select source] --> B[Draft script]
    B --> C[Voiceover plan]
    C --> D[Visual asset plan]
    D --> E[Subtitles]
    E --> F[Render plan]
    F --> G[Quality check]
    G --> H{Explicit upload approval?}
    H -->|No| I[Stop before upload]
    H -->|Yes| J[Upload step listed in plan]
```

File: `src/showcase/video_workflow.py`. The output is only a plan; neither rendering nor uploading is performed.

## 4. Company directory

```mermaid
flowchart TD
    A[Company records] --> B[Validate/construct typed records]
    B --> C[Sort by confirmed promotional amount]
    C --> D[Tie-break by timestamp]
    D --> E[Stable ID tie-break]
    E --> F[Promotional directory order]
```

File: `src/showcase/company_directory.py`. The demo ranking represents promotional support only, not a quality assessment.

## 5. Image upload validation

```mermaid
flowchart TD
    A[Filename, MIME type, size] --> B{Filename present?}
    B -->|No| X[Reject]
    B -->|Yes| C{Allowed MIME?}
    C -->|No| X
    C -->|Yes| D{Size within limit?}
    D -->|No| X
    D -->|Yes| E[Metadata accepted]
    E --> F[Production must inspect and decode bytes safely]
```

File: `src/showcase/photo_upload.py`. Metadata validation alone does not establish that a file is a safe image.

## 6. Market-data alert

```mermaid
flowchart TD
    A[Chronological synthetic observations] --> B[Validate positive prices and nonnegative volume]
    B --> C[Compute close-to-close percentage change]
    C --> D[Compare latest volume to prior average]
    D --> E{Both thresholds passed?}
    E -->|Yes| F[Alert-only result]
    E -->|No| G[No alert]
```

File: `src/showcase/market_data.py`. No broker adapter or order-execution function exists in this showcase.
