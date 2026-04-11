"""
Summary – 5 Logic Exercises (Day 5)

1 Sum of Two Numbers
The user inputs two values, and the program adds them and displays the result.
This exercise trains input handling, type conversion (int), and basic arithmetic operations.


num1 = float(input(f"Number 1: "))
num2 = float(input(f"Number 2: "))
print(f"{num1 + num2}")


2 Average of 4 Grades
The user inputs four grades, and the program calculates the average.
This exercise focuses on working with variables and performing calculations.

n1 = float(input("Enter note 1: "))
n2 = float(input("Enter note 2: "))
n3 = float(input("Enter note 3: "))
n4 = float(input("Enter note 4: "))
print(f"Average = {(n1+n2+n3+n4)/4}")

3 Square Area
The user inputs the side length, and the program calculates the area of the square.
Formula: side × side
This exercise reinforces simple mathematical operations and variable usage.

side_length = float(input("Enter side length of the square: "))
print(f"Side x side = {side_length*side_length}")

4 Temperature Conversion
The user inputs a temperature in Celsius, and the program converts it to Fahrenheit.
Formula: F = (C × 9/5) + 32
This exercise practices applying formulas in code.

celsius = float(input("Enter temperature in Celsius: "))
print(f"{(celsius*9)/5 +32}")

5 Salary Calculation
The user inputs the hourly rate and the number of hours worked, and the program calculates the total salary.
Formula: salary = rate × hours
This exercise applies logic to a real-world scenario.
"""

hours = int(input("Enter the number of hours worked: "))
rate = float(input("Enter the hourly rate: "))
print(f"The total salary: ${hours*rate}")
