users = {}


def create_user(name="Name", age="", e_mail="useremail@user.com"):
    user_id = len(users) + 1
    users[user_id] = {"id": user_id, "name": name, "age": age, "e_mail": e_mail}


def get_all_users():
    return users


# create_user("Test1", 1, "usertestes.com")
# create_user("Test2", 2, "acapam.com")
# create_user("Test3", 3, "inseto.com")

# print(get_all_users())


def update_user():
    user = int(input("\nEnter the user you want to modify: "))
    if user not in users:
        print(f"\nPlease enter a valid user.\n")
    else:

        field = input("Enter what you want to change (name, age, e_mail): ")

        if field == "name":
            users[user][field] = input("Enter new name: ")

        elif field == "age":
            users[user][field] = input("Enter new age: ")

        elif field == "e_mail" or field == "email":
            users[user]["e_mail"] = input("Enter new e_mail: ")
        else:
            print("Invalid field.")

        print(f"User to be modified: {user}\n")


# update_user()
# print(get_all_users())
