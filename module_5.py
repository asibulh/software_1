#1
import random
num = int(input("How many dice to roll: "))
total = 0
for i in range(num):
    dice = random.randint(1, 6)
    total = total + dice
print("Sum of the dice:", total)


#2
numbers = []
num = input("Enter a number (empty to quit): ")
while num != "":
    numbers.append(float(num))
    num = input("Enter a number (empty to quit): ")
numbers.sort(reverse=True)
print("Five greatest numbers:")
i =0
while i < 5 and i < len(numbers):
    print(numbers[i])
    i=i+1


#3
num = int(input("Enter an integer: "))
is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break
if num >1 and is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")


#4
cities = []
for i in range(5):
    name=input("Enter city name: ")
    cities.append(name)
    print("Cities you entered:")
for city in cities:
    print(city)