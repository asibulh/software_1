#1

import random
def roll_dice():
    return random.randint(1, 6)
result =0
while result !=6:
    result= roll_dice()
    print(result)


#2

import random
def roll_dice(sides):
    return random.randint(1, sides)
sides = int(input("Enter number of sides on dice: "))
result = 0
while result != sides:
    result= roll_dice(sides)
    print(result)


#3

def gallon_to_litre(gallons):
    return gallons * 3.785
while True:
    gallons= float(input("Enter gasoline in gallons: "))
    if gallons <0:
        break
    litres=gallon_to_litre(gallons)
    print("Litres:",litres)


#4

def sum_list(numbers):
    total=0
    i=0
    while i<len(numbers):
        total=total + numbers[i]
        i = i + 1
    return total
numbers=[5, 10, 15, 20]
result=sum_list(numbers)
print("Sum:", result)


#5

def remove_odd(numbers):
    new_list= []
    i=0
    while i<len(numbers):
        if numbers[i] % 2==0:
            new_list.append(numbers[i])
        i = i + 1
    return new_list
numbers = [1,2,3,4,5,6,7,8]
even_numbers = remove_odd(numbers)
print("Original list:",numbers)
print("Even numbers list:",even_numbers)



#6

import math
def pizza_unit_price(diameter, price):
    radius= diameter/2
    area= math.pi*radius* radius
    area_m2= area/10000
    unit_price= price/area_m2
    return unit_price
d1= float(input("Enter diameter of first pizza (cm): "))
p1= float(input("Enter price of first pizza (€): "))
d2= float(input("Enter diameter of second pizza (cm): "))
p2= float(input("Enter price of second pizza (€): "))
price1= pizza_unit_price(d1,p1)
price2= pizza_unit_price(d2,p2)
if price1<price2:
    print("First pizza gives better value.")
else:
    print("Second pizza gives better value.")
