person = {}
for i in range(3):
    key = input("Enter a Key: ")
    value = input("Enter a value: ")
    person[key] = value

person.pop(input("Enter a key to remove: "))
print(person)
