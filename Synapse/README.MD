# Synapse

A command-line tool to track concepts, topics, and learning progress. Built from zero, growing alongside the developer who made it.

---

## What is Synapse?

Synapse creates connections between concepts. It lets you log what you're studying, how well you understand it, and where you stand, all from the terminal, all saved locally in a CSV file.

The idea: the tool grows with you. As your skills improve, so does Synapse.

---

## Features

- Add learning entries with category, topic, level, and status
- View a full report of all tracked concepts
- Update any field of an existing entry
- Delete entries by ID
- Data persists across sessions via a local CSV file

---

## Fields

| Field       | Description                                   |
|-------------|-----------------------------------------------|
| `id`        | Unique identifier for the entry               |
| `categoria` | Area of study (e.g. python, machine learning) |
| `argomento` | Specific topic (e.g. functions, regression)   |
| `livello`   | Difficulty level (e.g. base, intermedio)      |
| `stato`     | Current status (e.g. completato, in corso)    |
| `note`      | Free notes (e.g. course name, week)           |

---

## Usage

```bash
python synapse.py
```

```
--- SYNAPSE MENU ---
1) Aggiungi valore
2) Leggi report
3) Modifica valore
4) Cancella valore
5) Exit
```

---

## Example Entry

```
ID: 001 | Categoria: python | Argomento: funzioni | Livello: base | Stato: completato | Note: cs50p week2
```

---

## Tech Stack

- Python 3.12+
- `csv` module (standard library)
- No external dependencies

---

## Project Context

Synapse was built during [CS50P](https://cs50.harvard.edu/python/) - Harvard's Introduction to Programming with Python - as part of a self-directed path from zero background toward AI development.

The project lives in [`cs50p-python`](https://github.com/boccassinisergio-afk/cs50p-python), a public repo documenting the full learning journey.

---

## Roadmap

- [ ] Auto-generated IDs
- [ ] Filter report by category or status
- [ ] Progress statistics
- [ ] Export to Markdown or HTML
- [ ] JSON backend

---

## Author

Built by Sergio Boccassini , transitioning into AI development, one project at a time.
