# Revenue Report
#
#
#
# Write a function that gets user to input the monthly revenues for the past quarters.
# It then returns a variable of list data type to caller with the corresponding values.
# Then generate a revenue report denoting the month, revenue, and cumulative total for each month.
# It ends with a message that sums up the total revenue. Appropriate formatting has to be in place for numeric numbers (decimals and comma) and spacing.
# The output may look like the following.

def revenue_report():
    months = [1,2,3]
    cummulative_total = []
    monthly_revenue = []
    for i in range(1, len(months)+1):
        user_input = float(input("Enter  Revenue for month {}: ".format(i)))
        monthly_revenue.append(user_input)
        cummulative_total.append(sum(monthly_revenue))

    print("""Revenue Report
---------------------------""")
    for index,element in enumerate(monthly_revenue):
        print("Revenue for {}: $ {:.2f} | Cummulative. Total: $ {:.2f}".format(int(index+1),element,cummulative_total[index]))

    print("The company has made a total of $ {:.2f} in the last quarter.".format(cummulative_total[-1]))


revenue_report()
