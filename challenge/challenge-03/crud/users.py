users = {}


def create_user(name="Name", age=int, e_mail="useremail@user.com"):
    user_id = len(users) + 1
    name = input("Enter a name: ")
    age = int(input("Enter an age: "))
    e_mail = input("Enter an e-mail: ")

    users[user_id] = {"name": name, "age": age, "e_mail": e_mail}
