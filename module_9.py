#1

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

# Main program

car = Car("ABC-123", 142)

print("Registration number:", car.registration_number)
print("Maximum speed:", car.max_speed)
print("Current speed:", car.current_speed)
print("Travelled distance:", car.travelled_distance)


#2

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

# Main program

car = Car("ABC-123", 142)

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)

print("Current speed after acceleration:", car.current_speed)

car.accelerate(-200)
print("Speed after emergency brake:", car.current_speed)


#3

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

# Example

car = Car("ABC-123", 142)
car.current_speed = 60
car.travelled_distance = 2000

car.drive(1.5)
print("Travelled distance:", car.travelled_distance)  #2090


#4


import random
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

# Create cars

cars = []
for i in range(1, 11):
    reg_number = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    cars.append(Car(reg_number, max_speed))

# Race loop

race_finished = False

while not race_finished:
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)

        if car.travelled_distance >= 10000:
            race_finished = True

# Print results

print(f"{'Reg Number':<10} {'Max Speed':<10} {'Speed':<10} {'Distance':<15}")
print("-" * 50)

for car in cars:
    print(f"{car.registration_number:<10} {car.max_speed:<10} "
          f"{car.current_speed:<10} {car.travelled_distance:<15.2f}")