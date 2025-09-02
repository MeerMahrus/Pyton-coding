m = input("Enter your gender: ").lower()


if m == "male":
    n = int(input("Enter your age: "))
    if n > 21:
        print("You can have your licence")
    else:
        print("You can not have yur licence")
elif m == ("female"):
    n = int(input("Enter you age"))
    if n > 18:
        print("You can have your licence")
    else:
        print("You can not have tour licence")
else:
    print("That is not a gender please put an appropriate gender")
           