user_monthly_income = float(input("Enter your monthly income: "))
user_monthly_expense = float(input("Enter your monthly income: "))

monthly_savings = user_monthly_income - user_monthly_expense

print(f"Your monthly savings are ${monthly_savings}.")

annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Projected Savings after one year, with interest, is: ${annual_savings}")



