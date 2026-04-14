largest = 0
for i in range(5):
    number = float(input("Enter a number: "))
    if number > largest:
        largest = number
print(f"{largest}")
