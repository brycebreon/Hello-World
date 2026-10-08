# Bryce Breon 
# 09/09/2026
# homework 1

#1. Sales Tax Calculator 

price = float(input("Enter the item's price: "))

quantity = int(input("Enter the quantity: "))

tax_rate = 0.075

subtotal = price * quantity
tax_amount = subtotal * tax_rate
total = subtotal + tax_amount

print("Subtotal:", round (subtotal, 2))
print ("Tax amount:", round (tax_amount, 2))
print ("Total:", round(total, 2))


print ("---" * 20)

#2 Employee weekly pay calculator 

hourly_wage = float(input("Enter hourly wage: "))
hours_worked = float(input("Enter total hours worked: "))

if hours_worked > 40:
    base_pay = hourly_wage * 40
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * hourly_wage * 1.5
else:
    base_pay = hourly_wage * hours_worked
    overtime_pay = 0
    
total_pay = base_pay + overtime_pay

print ("Base pay:", round (base_pay, 2))
print ("Overtime pay:", round (overtime_pay, 2))
print ("Total pay:", round (total_pay, 2))


print ("---" * 20)

#3 Student Grade Categorizer

numeric_grade = float(input("Enter your numeric grade: "))

if numeric_grade >= 90:
    letter_grade = "A"
elif numeric_grade >= 80:
    letter_grade = "B"
elif numeric_grade >= 70:
    letter_grade = "C"
elif numeric_grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
    
print ("Numeric grade:", numeric_grade)
print ("Letter grade:", letter_grade) 


print ("---" * 20)

#4 Bonus Eligibility Checker 

hours_worked = float(input("Enter hours worked: "))
performance_score = float(input("Enter performance score: "))

BONUS = 100

if hours_worked > 35 and performance_score > 85:
    print("Congratulations! You earned a bonus of $", BONUS)
else: 
    if hours_worked <= 35:
        hours_needed = 36 - hours_worked
        print("You need", hours_needed, "more hours.")
        
    if performance_score <= 85:
        points_needed = 86 - performance_score
        print("You need", points_needed, "more performance points.")
    