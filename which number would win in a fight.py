W = int(input("Enter a your number: "))
I = int(input("Enter a your number: "))
N = int(input("Enter a your number: "))

if W > I and W > N:
    print("The Winner is....",W)
elif I > W and I > N:
    print("The Winner is....",I)
else:
    print("The Winner is....",N)
