leap = int(input("Enter a year!: "))

if leap % 400 == 0:
    print("That year is a leap year, one extra day of school :(")
elif leap % 100 == 0:
    print("That year is not a leap year, Febuary is sad :0")
elif leap % 4 == 0:
    print("That year is a leap year, one extra day of school :(")
else:
    print("That year is not a leap year, February is sad :0")