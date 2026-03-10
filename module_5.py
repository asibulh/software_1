import random
num = int(input("How many dice to roll: "))
total = 0
for i in range(num):
    dice = random.randint(1, 6)
    total = total + dice
print("Sum of the dice:", total)



