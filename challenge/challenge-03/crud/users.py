users = {}


def create_user(name="Name", age="", e_mail="useremail@user.com"):
    user_id = len(users) + 1
    name = input("Enter new name: ")
    age = input("Enter new age: ")
    e_mail = input("Enter new e_mail: ")
    users[user_id] = {"name": name, "age": age, "e_mail": e_mail}


def get_all_users():
    return users


def update_user():
    user_id = int(input("\nEnter the user you want to modify: "))
    if user_id not in users:
        print(f"\nPlease enter a valid user.\n")
    else:

        field = input("Enter what you want to change (name, age, e_mail): ")

        if field == "name":
            users[user_id][field] = input("Enter new name: ")

        elif field == "age":
            users[user_id][field] = input("Enter new age: ")

        elif field == "e_mail" or field == "email":
            users[user_id]["e_mail"] = input("Enter new e_mail: ")
        else:
            print("Invalid field.")

        print(f"User to be modified: {user_id}\n")


def delete_user():
    user_id = int(input("\nEnter the user you want to delete: "))
    if user_id not in users:
        print(f"\n Please enter a valid user.")
    else:
        del users[user_id]


while True:
    print(
        f" 1 - Add new user.\n 2 - List all users.\n 3 - Update a user.\n 4 - Delete a user.\n 5 - Exit."
    )
    option = input("Enter an opition: ")
    if option == "1":
        user = int(input("Enter the number of new users: "))

        for i in range(user):
            create_user()

    elif option == "2":
        all_users = get_all_users()

        for user_id, dados in all_users.items():
            print(
                f"\n ID:{user_id}\n Name:{dados['name']}\n Age:{dados['age']}\n E_mail:{dados['e_mail']}\n____________\n"
            )


# create_user("Test1", 1, "usertestes.com")
# create_user("Test2", 2, "acapam.com")
# create_user("Test3", 3, "inseto.com")


# print("\ncarregando.")
# print("carregando..")
# print("carregando...\n")

# print(get_all_users())

# print("\ncarregando.")
# print("carregando..")
# print("carregando...")

# update_user()

# print("\ncarregando.")
# print("carregando..")
# print("carregando...")

# print(get_all_users())


# print("\ncarregando.")
# print("carregando..")
# print("carregando...")

# delete_user()

# print("\ncarregando.")
# print("carregando..")
# print("carregando...")

# print(get_all_users())

# print("\ncarregando.")
# print("carregando..")
# print("carregando...")

# print("Encerrado")
