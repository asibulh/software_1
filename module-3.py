#1
length = float(input("Enter the length of the zander in centimeters: "))
if length < 42:
    difference = 42 - length
    print("Release the fish back into the lake.")
    print("It is", difference, "cm below the size limit.")
else:
    print("The fish meets the size limit.")




#2
cabin = input("Enter the cabin class (LUX, A, B, C): ")
if cabin == "LUX":
    print("Upper-deck cabin with a balcony.")
elif cabin == "A":
    print("Above the car deck, equipped with a window.")
elif cabin == "B":
    print("Windowless cabin above the car deck.")
elif cabin == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")




#3
gender = input("Enter biological gender (male/female): ")
hb = float(input("Enter hemoglobin value (g/l): "))
if gender == "female":
    if hb < 117:        print("Hemoglobin level is low.")
    elif hb <= 155:        print("Hemoglobin level is normal.")
    else:        print("Hemoglobin level is high.")
elif gender == "male":
    if hb < 134:        print("hemoglobin level is low.")
    elif hb <= 167:        print("hemoglobin level is normal.")
    else:        print("hemoglobin level is high.")
else:    print("Invalid gender.")





#4
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
        print(f"{year} is not a leap year.")
