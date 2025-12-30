import random

def random_number():
    return random.randint(1, 10)

def get_a_number():
    
     while True:
        try:
            guess = int(input("Enter your guess (1 to 10)"))
            if 1 <= guess <= 10 :
                return guess
            else:
                print("This is not a number from 1 to 10")
        except ValueError:
             print("Invalid Input")