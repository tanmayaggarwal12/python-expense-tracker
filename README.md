# Expense Tracker

A small command-line app that checks whether your spending stays inside your budget. You type a budget, list where your money went and how much, and the app shows the total, average, highest and lowest expense, and tells you if you are still within your limit.

This is my project for the VITyarthi *Build Your Own Project* evaluation. I first wrote it as one script (`expense_tracker.py`) plus a `main.py`, then split the same code into separate files so each one has a single job.

## Features

- **Set a budget** – `set_global_budget()` asks for your budget and rejects anything that is not a number.
- **Enter expenses** – type the areas (`food travel rent`) and the amounts (`800 250 3000`) separated by spaces.
- **Analysis** – total, average, highest and lowest expense.
- **Budget check** – shows the money left, or warns that you went over.
- **Input validation** – wrong numbers or mismatched counts print `Invalid input` instead of crashing.
- **Repeat rounds** – after each round, type `yes` or `y` to go again, or `no` or `n` to quit.
- **Runtime storage only** – everything is kept in memory while the program runs. Nothing is saved to a file or database, so all data is gone when you quit.

## Technologies used

- Python 3.8 or newer (tested on 3.12)
- No external libraries – nothing to install
- Git and GitHub for version control

## Project structure

```
expense-tracker/
├── main.py                  # entry point
├── app/
│   ├── __init__.py
│   ├── expense_tracker.py   # spent_analysis() and loop_spent_analysis()
│   ├── budget.py            # set_global_budget() and check_budget()
│   ├── expense_input.py     # get_expense_lists()
│   ├── analysis.py          # calculate_expenses()
│   └── report.py            # show_report()
├── docs/                    # diagrams, screenshots, project report
├── statement.md
└── README.md
```

## How to install and run

```bash
git clone <your-repo-url>
cd python-expense-tracker
python main.py
```

Example session:

```
------------ Start Tracking Expenses ------------
--------------------------------------------------
Enter your budget: 5000
The area of spent [Write the area of spent with spaces]: food travel rent snacks
The amount of money spent [Write the expenditure with spaces]: 800 250 3000 150
**************************************************
Total calculated: ₹ 4200
Spent_list:  ['food', '800', 'travel', '250', 'rent', '3000', 'snacks', '150']
Average expense: ₹ 1050.0
Highest expense ₹ 3000
Lowest expense ₹ 150
You are within your budget! Remaining money:  ₹ 800.0
If you want to use expense tracker type yes or y or not want then type no or n n
Goodbye!
```

**Things to know**

- Nothing is saved between runs. Each round starts fresh.
- Area names are split on spaces, so use one word per area (`eating_out`, not `eating out`).
- Amounts must be whole numbers, so `250.5` is rejected as invalid input.

## How to test

The project is tested by running it and checking the output by hand. Run `python main.py` and try these:

| What to try | Expected result |
|---|---|
| Budget `5000`, areas `food travel rent snacks`, amounts `800 250 3000 150` | Total 4200, average 1050.0, highest 3000, lowest 150, remaining 800.0 |
| Budget `1000`, areas `food rent`, amounts `400 900` | Warning that the budget is exceeded |
| Budget `500`, areas `food`, amounts `500` | Within budget, remaining 0.0 |
| Budget `abc` | `Invalid Input`, then back to the yes/no question |
| Areas `food travel`, amounts `100` | `Invalid input` (counts do not match) |
| Amounts `100 abc` | `Invalid input` |


## Documentation

- `statement.md` – problem statement, scope, target users, features
- `docs/` – architecture, workflow, use case, component and sequence diagrams, and the full project report
