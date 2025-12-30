def tri (base, height):
    area = (base*height) / 2
    return area

base = float(input("Enter your base: "))
height = float(input("Enter your height: "))

res = tri (base , height)
print (res)