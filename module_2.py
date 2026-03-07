name = input("Enter your name: ")
print("Hello,", name+ "!")


import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius * radius
print("The area of the circle is:", area)



length = float(input("Enter the length of the circle: "))
width = float(input("Enter the width of the circle: "))
area = length * width
perimeter = (length + width) * 2
print("The area of the circle is:", area)
print("The perimeter of the circle is:", perimeter)



num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
sum = num1 + num2 + num3
product = num1 * num2 * num3
avarage = sum / 3
print("The sum is:", sum)
print("The product is:", product)
print("The average is:", avarage)




talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))
total_lots = talents * 20 * 32 + pounds * 32 + lots
grams = total_lots * 13.3
kilograms = int(grams // 1000)
remaining_grams = grams % 1000
print("The weight in modern units:")
print(f"{kilograms} kilograms and {remaining_grams:.2f} grams.")