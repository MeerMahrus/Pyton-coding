def rec (length, width):
    area = length*width 
    return area 

length = float(input("Enter a lenght"))
width = float(input("Enter a width"))

result = rec (length, width)
print(result)