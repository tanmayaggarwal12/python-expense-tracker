"""Expense input module: reads the areas and amounts typed by the user."""


def get_expense_lists():
    """Ask for the areas and the amounts (both separated by spaces).

    Returns (spent_area, spent_money) as two lists, or None if the input is invalid.
    The lists only exist in memory while the program is running.
    """
    area_of_spent = input("The area of spent [Write the area of spent with spaces]: ")
    spent_area = area_of_spent.split()

    money_spent = input("The amount of money spent [Write the expenditure with spaces]: ")
    spent_money = money_spent.split()

    # Both lists must have the same length and must not be empty
    if len(spent_area) == len(spent_money) and len(spent_area) > 0:
        return spent_area, spent_money

    print("Invalid input")
    return None
