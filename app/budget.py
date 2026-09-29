"""Budget module: asking for the budget and checking spending against it."""


def set_global_budget():
    """Ask the user for a budget. Returns the budget, or None if the input was invalid."""
    try:
        print("-" * 50)
        global_budget = float(input("Enter your budget: "))
        return global_budget
    except ValueError:
        print("Invalid Input")
        return None


def check_budget(total_sum, global_bgt):
    """Compare the total spent with the budget and tell the user the result."""
    if total_sum <= global_bgt:
        print("You are within your budget! Remaining money: ", "₹", global_bgt - total_sum)
    else:
        print("Warning: You have exceeded your budget!")
