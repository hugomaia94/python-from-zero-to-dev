import database as db

while True:
    print(
        f" 1 - Add new user.\n 2 - List all users.\n 3 - Update a user.\n 4 - Delete a user.\n 5 - Exit."
    )
    option = input("Enter an opition: ")
    if option == "1":
        user = int(input("Enter the number of new users: "))

        for i in range(user):
            db.create_user()
            print("\n")

    elif option == "2":
        all_users = db.get_all_users()

        for user_id, dados in all_users.items():
            print(
                f"\n ID:{user_id}\n Name:{dados['name']}\n Age:{dados['age']}\n E_mail:{dados['e_mail']}\n____________\n"
            )
    elif option == "3":
        db.update_user()
