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
