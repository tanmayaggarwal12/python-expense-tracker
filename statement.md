# Problem Statement

## The problem

Most students and first-time earners have a rough idea of what they spend, but they rarely add it up. Money quietly goes on food, travel and small things, and by the end of the month the budget is gone without them knowing where it went. Spreadsheets and full budgeting apps work, but they need more setup than people want for a quick check.

This project gives a fast way to answer three simple questions: *How much did I spend? Where did most of it go? Am I still within my budget?*

## Scope

**Included**

- Setting a budget for a round of tracking
- Entering several expenses at once (area + amount)
- Calculating total, average, highest and lowest expense
- Comparing the total against the budget
- Handling invalid input with a clear message
- Keeping data in memory only while the program runs
- Running multiple rounds in one session

**Not included (for now)**

- Saving expenses between sessions (no database, no files: everything is runtime storage only)
- Decimal amounts and multi-word category names
- Dates, monthly reports or charts
- A graphical or web interface

## Target users

- Students managing pocket money or a monthly allowance
- Anyone who wants a quick spending check without installing a full budgeting app
- Beginners who want a small, readable example of a modular Python project

## High-level features

1. Budget setting
2. Bulk expense entry
3. Spending analysis (total, average, highest, lowest)
4. Budget status: remaining money or an exceeded warning
5. `Invalid input` handling instead of crashes
6. Simple runtime (in-memory) storage, nothing saved
7. Repeatable rounds from one run
