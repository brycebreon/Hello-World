# Bryce Breon
# 10/04/2026
# Homework 2

loan_amount = float(input("Enter the loan amount ($): "))
annual_rate = float(input("Enter the annual interest rate (%): "))
years = int(input("Enter the loan term (years): "))


annual_rate = annual_rate / 100
monthly_rate = annual_rate / 12


num_payments = years * 12


monthly_payment = (
    loan_amount
    * (monthly_rate * (1 + monthly_rate) ** num_payments)
    / ((1 + monthly_rate) ** num_payments - 1)
)


print(f"\nMonthly Payment: ${monthly_payment:,.2f}")


print(
    f"{'Month':>5} {'Payment':>10} {'Principal':>12} {'Interest':>10} {'Balance':>12}"
)


balance = loan_amount


for month in range(1, num_payments + 1):

    interest = balance * monthly_rate

    principal_paid = monthly_payment - interest

    balance = balance - principal_paid

    if balance < 0:
        balance = 0

    print(
        f"{month:5} {monthly_payment:10,.2f} {principal_paid:12,.2f} {interest:10,.2f} {balance:12,.2f}"
    )
