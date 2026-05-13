aux = 1
while aux != 0:
    print(f"\n=== MENU ===")
    print(f"1 - Show menu explanation")
    print(f"2 - Sum two numbers")
    print(f"3 - Check even or odd")
    print(f"4 - Exit")
    aux = int(input("Enter a number: "))
    if aux == 0:
        aux = 5

    elif aux == 1:
        print(f"\n\n--- MENU EXPLANATION ---")
        print(f"1 - Displays a description of all available options in the program.")
        print(f"2 - Prompts the user to enter two numbers and shows their sum.")
        print(
            f"3 - Prompts the user to enter a number and tells whether it is even or odd."
        )
        print(f"4 - Terminates the program.")
    elif aux == 2:
        num1 = float(input(f"Number 1: "))
        num2 = float(input(f"Number 2: "))
        print(f"{num1 + num2}")
    elif aux == 3:
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print(f"Number is even.")
        else:
            print(f"Number is odd.")
    elif aux == 4:
        print(f" Goodbye!")
        aux = 0
    else:
        print("ERROR!")
