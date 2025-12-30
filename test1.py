running = True 

while  running:
    n = input("Enter an number or type 'exit' to quit: ").lower()
    if n == "exit":
        running = False
        print("bye bye")
    else:
        n = int(n)
        if n % 2 == 0:
            print("THe number is even")
        else:
            print("The number is odd")