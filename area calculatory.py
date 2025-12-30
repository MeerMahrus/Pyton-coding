def tri (base, height):
    area = (base*height) / 2
    return area

def rec (lenght, width):
    area = lenght*width
    return area

def squ (side):
    area = side** 2
    return area

def cir (raduis):
    area = 3.14159 * raduis ** 2
    return area


print("====== AREA CALCULATOR ======")
print("                              ")
print("Chose any shape from the following:  ")
print("1.Rectangle")
print("2.Triangle")
print("3.Square")
print("4.Circle")

choice = int(input("Enter your chosen shape`s number: "))

if choice == 1:
    lenght = float(input("Enter your lenght: "))
    width = float(input("Enter your width: "))
    print("The area of rectangle is ",rec (lenght, width))
    
    
elif choice == 2:
    base = float(input("Enter your base: "))
    height = float(input("Enter your height: "))
    print("The area of triangle is ",tri (base, height))
    
    
elif choice == 3:
    side = float(input("Enter your side: "))
    print("The area of square is ",squ (side))
    
elif choice == 4:
    raduis = float(input("Enter your raduis: "))
    print("The area of circle is ",cir (raduis))
    
else:
    print("ERROR,That is not a number in the following.")