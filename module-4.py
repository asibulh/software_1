#1
number = 1
while number <= 1000:
 if number % 3 == 0:
    print(number)
 number= number + 1


#2
inches = float(input("Enter inches: "))
while inches >= 0:
    cm = inches * 2.54
    print("Centimeters:", cm)
    inches = float(input("Enter inches: "))


#3
num = input("Enter a number: ")
smallest= None
largest= None
while num != "":
    number = float(num)
    if (smallest is None
    or number < smallest):
     smallest = number
     if (largest is None
     or number > largest):
      largest = number
      num = input("Enter a number: ")
print("Smallest number:", smallest)
print("Largest number:", largest)


#4
import random
number = random.randint(1, 10)
guess = int(input("Guess the number between 1 and 10: "))
while guess != number:
    if guess > number:
        print("Too high")
    else:
        print("Too low")
    guess = int(input("Guess again: "))
print("Correct")


#5
username = "python"
password = "rules"
attempt = 0
while attempt <5:
    user= input("Username: ")
    pw = input("Password: ")
    if user == username and pw == password:
        print("Welcome")
        attempt = 5
    else:
        print("Incorrect username or password")
        attempt = attempt + 1
    if attempt == 5 and (user != username or pw != password):
        print("Access Denied")



#6
import random
N = int(input("How many random points: "))
count = 0
inside = 0
while count < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x*x + y*y < 1:
        inside = inside + 1
    count = count + 1
pi = 4 * inside / N
print("Approximation of pi:", pi)