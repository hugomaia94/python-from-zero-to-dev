even = 0
for i in range(5):
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        even += 1
print(f"{even} even numbers.")
