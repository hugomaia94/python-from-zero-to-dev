users = {}


def create_user(name="Name", age="", e_mail="useremail@user.com"):
    user_id = len(users) + 1
    users[user_id] = {"name": name, "age": age, "e_mail": e_mail}


def get_all_users():
    return users
