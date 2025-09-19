monthly_income = float(input("Enter your monthly income: "))

monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

annual_savings_no_interest = monthly_savings * 12

projected_annual_savings = annual_savings_no_interest + (annual_savings_no_interest * 0.05)

print("\nYour monthly savings are:", monthly_savings)

print("Your projected annual savings after one year are:", projected_annual_savings)