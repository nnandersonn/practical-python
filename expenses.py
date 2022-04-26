expenses = []

count = int(input('How many reciepts do you have to enter?\n'))

for x in range(count):
    num = input('Enter daily expense\n')
    expenses.append(float(num))
    print(expenses)




sum = sum(expenses)


print('you spent', sum)