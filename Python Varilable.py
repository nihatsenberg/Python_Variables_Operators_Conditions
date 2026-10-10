# Task 1
print('Task 1: Compare two numbers')
a=int(input('Enter a number: '))
b=int(input('Enter another number: '))
if a > b:
    print(f'{a} is greater than {b}')
elif b > a:
    print(f'{b} is greater than {a}')
else:
    print(f'{a} and {b} are equal')

#Task 2
print('Task 2: Check if a number is positive, negative or zero')
c = int(input('Enter a number: '))
if c > 0:
    print(f'{c} is positive')
elif c < 0:
    print(f'{c} is negative')
else:
    print(f'{c} is zero')

#Task 3 
print('Task 3: Check if a number is even or odd')
a = int(input('Enter a number: '))
if a % 2 == 0:
    print(f'{a} is even')
else:
    print(f'{a} is odd')

#Task4
print('Task 4: Determine grade based on score')
score = int(input('Enter your score: '))
if 0 <= score <= 100:
    if score >= 91:
        print('Grade: A')
    elif score >= 81:
        print('Grade: B')
    elif score >= 71:
        print('Grade: C')
    elif score >= 61:
        print('Grade: D')
    elif score >= 51:
        print('Grade: E')
    elif score < 51:
        print('Grade: F')
    else:
        print('Invalid score')

#Task 5
print('Task 5: Determine result based on exam score, school score and age')
a=int(input('Enter a number: '))
b=int(input('Enter another number: '))
c=int(input('Enter a third number: '))
if a > b and a > c:
    print(f'{a} is the greatest number')
elif b > a and b > c:
    print(f'{b} is the greatest number')
elif c > a and c > b:
    print(f'{c} is the greatest number')
else:
    print('All numbers are equal')

#Task 6
print('Task 6: Determine result based on exam score, school score and age')
first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))
operation = input('Enter the operation (+, -, *, /, % ,** , //): ')
if operation == '+':
    result = first_number + second_number
    print(f'The result of {first_number} + {second_number} is: {result}')
elif operation == '-':
    result = first_number - second_number
    print(f'The result of {first_number} - {second_number} is: {result}')
elif operation == '*':
    result = first_number * second_number
    print(f'The result of {first_number} * {second_number} is: {result}')
elif operation == '/':
    if second_number != 0:
        result = first_number / second_number
        print(f'The result of {first_number} / {second_number} is: {result}')
    else:
        print('Error: Division by zero is not allowed.')
elif operation == '%':
    if second_number != 0:
        result = first_number % second_number
        print(f'The result of {first_number} % {second_number} is: {result}')
    else:
        print('Error: Division by zero is not allowed.')
elif operation == '**':
    result = first_number ** second_number
    print(f'The result of {first_number} ** {second_number} is: {result}')
elif operation == '//':
    if second_number != 0:
        result = first_number // second_number
        print(f'The result of {first_number} // {second_number} is: {result}')
    else:
        print('Error: Division by zero is not allowed.')
else:
    print('Invalid operation. Please enter a valid operator (+, -, *, /, %, **, //).')

#Task 7
print('Task 7: Determine result based on exam score, school score and age')
age = int(input('Enter your age: '))
if age <= 12:
    print('You are a child')
elif 13 <= age <= 17:
    print('You are a teenager')
elif 18 <= age <= 64:
    print('You are an adult')
elif age >= 65:
    print('You are a senior')
else:
    print('Invalid age')

#task 8
print('Task 8: Calculate discount based on total purchase amount')
total = float(input('Enter the total purchase amount: '))
if total < 100:
    rate = 0
elif total < 300:
    rate = 10
elif total < 500:
    rate = 15
else:
    rate = 20
discount = total * rate / 100
print('Original price:', total)
print('Discount:', discount)
print('Final price:', total - discount)

#Task 9
print('Task 9: Determine result based on exam score, school score and age')
a=int(input('Enter a number: '))
b=int(input('Enter another number: '))
c=int(input('Enter a third number: '))
if a > b and a > c:
    if b > c:
        print(f'The numbers in descending order are: {c}, {b}, {a}')
    else:
        print(f'The numbers in descending order are: {b}, {c}, {a}')
if b > a and b > c:
    if a > c:
        print(f'The numbers in descending order are: {c}, {a}, {b}')
    else:
        print(f'The numbers in descending order are: {a}, {c}, {b}')
if c > a and c > b:
    if a > b:
        print(f'The numbers in descending order are: {b}, {a}, {c}')
    else:
        print(f'The numbers in descending order are: {a}, {b}, {c}')

#Task 10
print('Task 10: ATM Withdrawal Simulation')
print('Your account balance is 1000 AZN.')
a = int(input('Enter the amount you want to withdraw: '))
if a == 0 or a < 0:
    print('Invalid amount. Please enter a positive value.')
elif a > 1000:
    print('Insufficient funds. You cannot withdraw more than your account balance.')
else:
    new_balance = 1000 - a
    print(f'You have successfully withdrawn {a} AZN. Your new account balance is {new_balance} AZN.')

#task 11
print('Task 11: Calculate electricity bill based on monthly usage')
usage = float(input("Monthly usage (kWh): "))
if usage < 0:
    print("Invalid input")
else:
    if usage <= 100:
        rate = 0.08
    elif usage <= 300:
        rate = 0.12
    else:
        rate = 0.15
    bill = usage * rate
    print("Usage:", usage, "kWh")
    print("Applied rate:", rate, "AZN per kWh")
    print("Total bill:", bill, "AZN")

#Task 12
print('Task 12: Calculate taxi fare based on distance')
start_fee = 2
distance = float(input("Distance (km): "))
if distance < 0:
    print("Invalid distance")
else:
    if distance <= 5:
        distance_fee = distance * 0.70
    elif distance <= 15:
        distance_fee = 5 * 0.70 + (distance - 5) * 0.60
    else:
        distance_fee = 5 * 0.70 + 10 * 0.60 + (distance - 15) * 0.50
    total_fare = start_fee + distance_fee
    print("Starting fee:", start_fee, "AZN")
    print("Distance fee:", distance_fee, "AZN")
    print("Total amount:", total_fare, "AZN")

#Task 13
print('Task 13: Determine loan eligibility based on age, monthly salary and loan amount')
age = int(input("Enter your age: "))
monthly_salary = float(input("Enter your monthly salary: "))
loan_amount = float(input("Enter the loan amount you want to apply for: "))
if age < 18:
    print('You are not eligible to apply for a loan. Minimum age requirement is 18.')
if monthly_salary <= 500:
    print('You are not eligible to apply for a Loan')
if loan_amount > monthly_salary * 10:
    print('You are not eligible to apply for a Loan')
else:
    print('You are eligible to apply for a Loan')

#Task 14
print('Task 14: Determine triangle type based on side lengths')
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter a third number: "))
if a + b > c:
    if a + c > b:
        if b + c > a:
            if a == b:
                if b == c:
                    print("Equilateral")
                else:
                    print("Isosceles")
            else:
                if a == c:
                    print("Isosceles")
                elif b == c:
                    print("Isosceles")
                else:
                    print("Scalene")
        else:
            print("Triangle cannot be created")
    else:
        print("Triangle cannot be created")
else:
    print("Triangle cannot be created")

#Task 15
print('Task 15: Determine result based on exam score, school score and age')
if age < 16:
    print('Result: Rejected')
    print('Reason: Age is below 16')
elif exam_score < 0:
    print('Invalid exam score')
elif exam_score > 700:
    print('Invalid exam score')
elif school_score < 0:
    print('Invalid school score')
elif school_score > 100:
    print('Invalid school score')
elif exam_score >= 600:
    print('Result: Scholarship')
    print('Reason: Exam score is 600 or above')
elif exam_score >= 450:
    print('Result: Accepted')
    print('Reason: Exam score is 450-599')
elif exam_score >= 300:
    if school_score >= 80:
        print('Result: Accepted')
        print('Reason: Exam score 300-449 and school score is 80 or above')
    else:
        print('Result: Rejected')
        print('Reason: School score is below 80')
else:
    print('Result: Rejected')
    print('Reason: Exam score is below 300')
