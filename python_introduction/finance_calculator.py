income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your monthly expenses: "))
monthly_savings = income - expenses
projected_annual_savings = monthly_savings * 12 + (monthly_savings * 0.05 * 12)
print("Projected Annual Savings:", projected_annual_savings)
