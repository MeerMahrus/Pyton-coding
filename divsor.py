number = int(input("Enter your number "))
disor  = int(input("Eneter your divisor"))

if disor == 0:
    print("The divisor cannot be 0")
elif number % disor == 0:
    print(f"{number}is divided by{disor}")
else:
    print(f"{number}is not divisible")