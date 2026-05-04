# Call Outcome Tracker – CS50P Week 4

A Python program to record and report the outcome of customer service calls, tracking sales made and issues reported, with persistent storage across sessions.

Built as a personal project to reinforce the topics covered in Week 4 of Harvard's CS50P (Libraries, APIs, JSON).

---

## Features

- Log sales made during each call
- Log one or more issues per call
- Data persists in a local JSON file that is accessible at end of day or on subsequent days
- Daily report with a summary of all recorded calls

---

## How to run

```bash
python call_outcome_tracker.py
```

## Menu

| Option | Action |
|--------|--------|
| `1` | Record a sale |
| `2` | Enter one or more issues (type `Exit` to return to main menu) |
| `3` | View the daily report |
| `4` | Exit |

---

## Technologies

- Python
- JSON (for persistent local storage)

---

## What I learned

- Reading and writing JSON files with the `json` module
- Designing an interactive CLI menu
- Structuring data for daily reporting across multiple sessions

---

*Part of my CS50P learning journey – [@boccassini_ai](https://x.com/boccassini_ai)*
