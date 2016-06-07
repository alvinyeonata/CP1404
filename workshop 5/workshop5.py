"""
incomes = []
months = int(input("How many months? "))

for month in range(1, months + 1):
    income = float(input("Enter income for month " + str(month) + ": "))
    incomes.append(income)

print("\nIncome Report\n-------------")

total = 0
for month in range(1, months + 1):
    income = incomes[month - 1]
    total += income
    print("Month {:2d} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


numbers= 5
list=[]

for i in range(numbers):
    num = int(input("Number: "))
    list.append(num)

print("the first number is {}".format(list[0]))
print("the last number is {}".format(list[-1]))
print("the smallest number is {} ".format(min(list)))
print("the largest number is {}".format(max(list)))
print("The average of the numbers is", sum(list) / len(list))

"""
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username=input("Enter your username")
while username == username:
    if username in usernames:
        print("Access granted")
        break
    else:
        print("Acess denied")
        username = input("Enter your username")
