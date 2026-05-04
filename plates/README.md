# Vanity Plates – CS50P Week 2

A Python program that validates personalized (vanity) license plates based on a fixed set of rules.

This is my solution to the *Vanity Plates* problem from Harvard's CS50P, Week 2 – Loops.

---

## What it does

The program asks the user to enter a plate string and returns `Valid` or `Invalid` based on the following rules:

| Rule | Detail |
|------|--------|
| Length | Between 2 and 6 characters |
| First two characters | Must be letters |
| Numbers | Can only appear at the end |
| Leading zeros | Not allowed (e.g. `CS01` is invalid) |
| Special characters | Not allowed |

---

## How to run

```bash
python plates.py
```

Example:

Plate: CS50
Valid
Plate: CS05
Invalid

---

## What I learned

- Iterating over strings with `enumerate()`
- Boolean logic for multi-condition validation
- Decomposing a complex rule set into a single clean function

---

*Part of my CS50P learning journey – [@boccassini_ai](https://x.com/boccassini_ai)*