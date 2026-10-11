#Q. Only children between the age of 10 and 15 (both inclusive) are allowed to take a ride at an amusement park. Write an expression for this check.
"""
age = int(input("What is your age? "))
if age >= 10 and age <= 15:
    print("You're good to go! have fun!")
else:
    print("Sorry, but your age doesn't matchg the requirements. You can't ride this ride.")
"""
#Q. If each day of the week is represented with a number with Monday as 1, Tuesday as 2 and so on. Write an expression to check if it is a weekend.
number = int(input("Write down the day of the week in numerical form: "))
if number == 6 or number == 7:
    print("yay! its the weekend! :D")
elif number >= 8 or number <= 0:
    print("ERROR 404: this is not a day in the week :/")
else:
    print("it's not the weekend... :<")