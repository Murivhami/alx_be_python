# The objective of the task is to 
# calculate the user’s monthly savings based on inputted monthly income and expenses.

# User Input for Financial Details:
monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))

#Calculate monthly savings
monthly_savings =float( monthly_income) - float(total_monthly_expenses)

#Project Annual Savings
simple_annual_interest_rate = 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#Output results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
