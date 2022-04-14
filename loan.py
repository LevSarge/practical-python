# Get loan details
money_owed = float(input("How much money do you owe, in dollars?\n"))
apr = float(input("What is the annual percentage rate?\n"))
payment = float(input("WHat will your monthly payment be, in dollars?\n"))
months = int(input("How many months do you want to see results for?\n"))

#Divide the APR by 100 to get a percentage, then divide by 12 to get monthly rate
monthly_rate = apr/100/12

for i in range(months):
#Add interest
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    if (money_owed - payment < 0):
        print("The last payment is", money_owed)
        print("You paid off the loan in", i+1, "months")
        break

#Make the payment
money_owed = money_owed - payment

#Print monthly result
print("Paid", payment, "of which", interest_paid, "was interest")
print("Now I owe", money_owed)