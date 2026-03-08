age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to vote in Finnish parliamentary elections.")
else:
    remaining_years = 18 - age
    print("You are not old enough to vote.")
    print("You can vote after", remaining_years, "year(s).")

