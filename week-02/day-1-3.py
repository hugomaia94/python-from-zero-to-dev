num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
    print(f"{num1}")
else:
    if num1 < num2:
        print(f"{num2}")
    else:
        print(f"Equals.")
