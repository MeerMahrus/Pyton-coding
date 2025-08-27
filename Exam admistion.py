medical = input("Do you have any medical problem").lower()

if medical == "yes":
    attendence = int(input("What is your attendence: "))
    if attendence < 60:
        print("You are not allowed to give exam")
    else:
        print("Your are allowed to give exam")
elif medical == "no":
    attendence = int(input("What is your attendence: "))
    if attendence < 75:
        print("You are not allowed to give exam")
    else:
        print("Your are allowed to give exam")
else:
    print("Invalid input")