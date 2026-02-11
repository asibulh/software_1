age=int(input("enter your age:"))
if age>=18:
    print("you are old enough to vote in Finnish parliamentary elections.")
else:
    remaining_years=age-18
    print("you are not old enough to vote in Finnish parliamentary elections.")
    print("you can vote after",remaining_years, "year(s)")



