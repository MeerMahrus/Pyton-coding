mark = int(input("Enter your marks"))

if mark < 50:
    print("Your GPA is F-,You failed u did a very good job :(")
elif 50 <= mark <= 59:
    print("Your GPA is D,You almost failed try more serios next time")
elif 60 <= mark <= 69:
    print("Your GPA is C,You did bad but I think you can improve next time")
elif 70 <= mark <= 89:
    print("Your GPA is B,Your not that bad ")
elif 90 <= mark <= 100:
    print("Your GPA is A+,CONGRATES YOU SCORED AMAZING ")
else:
    print("ummm its not possible to get that mark ")