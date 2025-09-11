#Finanace calculator to calculate mothly income , monthly savings and Annual savings

monthly_income = input("Enter your monthly income:")

monthly_expenses = input("Enter your total monthly expenses:")

monthly_savings = monthly_income - monthly_expenses

projected_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("Your monthly savings are ","$",monthly_savings)

print("Projected savings after one year, with interest, is:","$",projected_annual_savings)


