# Manage Names → Create an empty list called names. Add 5 names using append. Remove one specific name using remove. Sort the list using sort and display the final result.

names = []
for i in range(5):
    name = str(input("Entar a name: "))
    names.append(name)
name = str(input("Enter a name to remove: "))
names.remove(name)
names.sort()
print(names)
