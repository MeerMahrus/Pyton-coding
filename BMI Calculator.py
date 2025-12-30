a = float(input("Enter your weight in KG: "))
b = float(input("Enter your height in metres: "))

m = a / b ** 2

print("Your BMI is:",m)

if m < 18.5:
    print("You are under weight, better start eating some burgers.")
elif 18.5 <= m <= 24.9:
    print("You have normal weight,you are pretty good at controling weight.Nice")
elif 25 <= m <= 29.9:
    print("You are over weight,I think you should stop eating burgers ")
elif 30 <= m <= 34.9:
    print("You are obese,you have to stop eating burgers you know! ")
else:
    print("YOU ARE EXTREMLY OBESE,STOP EATING BURGERS YOU WILL DIE!!!")