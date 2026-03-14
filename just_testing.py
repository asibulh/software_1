names=set()
name=input("Enter a Name: ")
while name !="":
    if name in names:
        print("Existing Name")
    else:
        print("New name")
        names.add(name)
    name = input("Enter a Name: ")
print("Names Entered:")
for n in names:
    print(n)