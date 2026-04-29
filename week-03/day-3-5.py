def user_data(name="User", age=0):
    person = {}
    person[name] = input("Enter a name: ")
    person[age] = int(input("Enter an age: "))
    return person


print(user_data())
