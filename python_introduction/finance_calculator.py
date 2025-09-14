monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
print("Your monthly savings are ", monthly_savings)
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 0.05 * 12)
print("Your projected annual savings are ", projected_annual_savings)