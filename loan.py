# Get loan details
money_owed = float(input("How much money do you ower, in dollers?\n")) # $50,000

apr = float(input('What is the annual percent rate?')) #3%

payment = float(input("what will your monthly payment be in dollars?"))#$1000

months = int(input("How many months do you wnat to see results for?"))#24

monthly_rate = apr/100/12

for i in range(months):
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    if (money_owed - payment < 0):
        print("The last payment is", money_owed)
        print("You paid off the load in", i+1, "months")
        break

    money_owed = money_owed - payment

    print("paid", payment, "of which", interest_paid, "was interest", end=' ')
    print("Now i ower", money_owed)