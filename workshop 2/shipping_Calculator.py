numberOfItem = float(input("Enter number of items"))
while numberOfItem <0:
    print("Invalid number of items!")
    numberOfItem = float(input("Enter number of items"))

costPerItem = float(input("Enter shipping cost per item"))
while costPerItem <0:
    print("Invalid shipping cost!")
    costPerItem = float(input("Enter shipping cost per item"))
shippingCost = numberOfItem * costPerItem
totalShippingCost= shippingCost
if totalShippingCost > 100:
    discount = totalShippingCost * 0.1
else:
    discount = 0

finalShippingCost = totalShippingCost - discount

print("$",finalShippingCost)