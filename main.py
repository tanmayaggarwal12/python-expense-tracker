"""Entry point for the Expense Tracker."""

from app import expense_tracker


def get_area_of_spent():
    # First round starts straight away
    expense_tracker.spent_analysis()


def get_loop_spent_analysis():
    # After that, the user decides whether to go again
    expense_tracker.loop_spent_analysis()


def main():
    print("-" * 12, "Start Tracking Expenses", "-" * 12)
    get_area_of_spent()
    get_loop_spent_analysis()


if __name__ == "__main__":
    main()
