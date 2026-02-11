age= int(input("enter your age:"))
if age>=18:
    print( "you are eligible to vote in Finnish parliamentary elections.")
else:
    remaining_years=age-18
    print( "you are not old enough to vote in Finnish parliamentary elections.")
    print("You can vote after", remaining_years, "years ago.")