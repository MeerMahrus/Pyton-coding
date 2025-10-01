run = True

while run:
    n = input("Enter a number or enter 'quit' to leave").lower()
    if n == "quit":
        print("bye bye")
        break
    n = int(n)
    if n % 2 == 0:
        print("This is even")
    else:
        print("This number is odd")