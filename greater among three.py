a = float(input("Enter a  number!"))
s = float(input("Enter a  number!"))
d = float(input("Enter a  number!"))

if a>s and a>d:
    print("The greatest number is",a)
elif s>a and s>d:
    print("The greater number is",s)
else:
    print("The gretest number is ",d)