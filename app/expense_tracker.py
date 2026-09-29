"""Main workflow: ties the budget, input, analysis and report modules together."""

from app import analysis, budget, expense_input, report


def spent_analysis():
    """One full round: budget -> expenses -> analysis -> report -> budget check."""
    try:
        global_bgt = budget.set_global_budget()
        if global_bgt is None:          # invalid budget, stop this round
            return

        expense_lists = expense_input.get_expense_lists()
        if expense_lists is None:       # invalid expenses, stop this round
            return
        spent_area, spent_money = expense_lists

        total_sum, avg, highest, lowest, expense_list = analysis.calculate_expenses(spent_area, spent_money)

        report.show_report(total_sum, expense_list, avg, highest, lowest)
        budget.check_budget(total_sum, global_bgt)
    except ValueError:
        print("Invalid input")


def loop_spent_analysis():
    """Keep offering another round until the user says no."""
    while True:
        choice = input("If you want to use expense tracker type yes or y or not want then type no or n ")

        if choice == "yes" or choice == "y":
            spent_analysis()
        else:
            print("Goodbye!")
            break
