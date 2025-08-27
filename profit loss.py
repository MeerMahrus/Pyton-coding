buy = int(input("Enter your buying price: "))
sell = int(input("Enter your selling price"))

if buy < sell:
    print("The profit is: ",sell - buy)
else:
    print("The loss is:",buy - sell)