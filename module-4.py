number = 1
while number <= 1000:
 if number % 3 == 0:
    print(number)
 number += 1



 while True:
     inches = float(input("Enter inches: "))
 if inches < 0:
     print("Program ended.")
     break
 cm = inches * 2.54
 print(cm, "centimeters")