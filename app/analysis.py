"""Analysis module: total, average, highest and lowest expense."""


def calculate_expenses(spent_area, spent_money):
    """Go through the expenses once and work out the summary numbers.

    Raises ValueError if any amount is not a whole number.
    Returns total_sum, avg, highest, lowest, expense_list.
    """
    expense_list = []
    total_sum = 0
    avg = 0
    highest = 0
    lowest = None

    for i in range(len(spent_area)):
        current_expense = int(spent_money[i])
        total_sum = total_sum + current_expense

        if current_expense > highest:
            highest = current_expense
        if lowest is None or current_expense < lowest:
            lowest = current_expense

        expense_list.append(spent_area[i])
        expense_list.append(spent_money[i])

    if len(spent_area) > 0:
        avg = total_sum / len(spent_area)

    return total_sum, avg, highest, lowest, expense_list
