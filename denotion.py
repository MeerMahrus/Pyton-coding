M = int(input("Enter the amount of taka:"))

note = M // 100
print("The amount of 100 Taka bills:",note)
M = M % 100


note = M // 50
print("The amount of 50 Taka bills:",note)
M = M % 50


note = M // 10
print("The amount of 10 Taka bills:",note)
M = M % 10


note = M // 5
print("The amount of 5 Taka bills:",note)
M = M % 5


note = M // 2
print("The amount of 2 Taka bills:",note)
M = M % 2


print("The amount of 1 Taka bills:",M)