#1

seasons=("Winter","Spring","Summer","Autumn")
month=int(input("Enter the number of a month(1-12): "))
if month==12 or month==1 or month==2:
    season=seasons[0]
elif month==3 or month==4 or month==5:
    season=seasons[1]
elif month==6 or month==7 or month==8:
    season=seasons[2]
elif month==9 or month==10 or month==11:
    season=seasons[3]
else:
    season="Invalid Month"
print("Season: ", season)



#2

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

