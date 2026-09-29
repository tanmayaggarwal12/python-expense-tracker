"""Report module: prints the results of the analysis."""


def show_report(total_sum, expense_list, avg, highest, lowest):
    print("*" * 50)
    print("Total calculated: ₹", total_sum)
    print("Spent_list: ", expense_list)
    print("Average expense: ₹", avg)
    print("Highest expense ₹", highest)
    print("Lowest expense ₹", lowest)
