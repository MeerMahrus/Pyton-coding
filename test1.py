a = int(input("Enter your weight in kg"))
b = int(input("Enter your height in metres"))

bmi = a / b**2
print(f"YOur bmi is{bmi:0.2f}")

if bmi < 18.5:
    print("you are underwieght")
elif 18.5 <= bmi <= 24.9:
    print("you have normal weight")
elif 25 <= bmi <=29.9:
    print("You are over weight")
elif 30 <= bmi <= 34.9:
    print("You are obse")
else:
    print("you are extermely obse")