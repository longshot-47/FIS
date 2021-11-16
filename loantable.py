'''
Filename: LoanTable.py

Date: 16-11-2021

Author: Ng Yat Lung

lab2 Q2 program to print loan table with payment schedule

	The loan amount is : 300
	The annual interest rate is: 12
	The monthly payment is: 100

		    Starting            Middle              Ending
	Month	Balance   Payment   Balance   Interest  Balance
	-------------------------------------------------------
	1.	300.00	  100.00    200.00       2.00   202.00	
	2.	202.00    100.00    102.00       1.02   103.02
	3.	103.02    100.00      3.02       0.03     3.05
	4.	  3.05      3.05      0.00       0.00     0.00
'''
amount = int(input('the load amount is: '))
rate = int(input('the annual interest rate is: '))
pay = int(input('the monthly payment is: '))

print('''
		Starting            Middle              Ending
	Month	Balance   Payment   Balance   Interest  Balance
    ''')

print('-'*55)

month = 1
starting_balance = amount
payment = pay
middle_balance = starting_balance - payment
interest = middle_balance * rate/12/100
ending_balance = middle_balance + interest
print("%-5d%10.2f%10.2f%10.2f%10.2f%10.2f"%
       (month, starting_balance, payment, middle_balance, interest, ending_balance))

while (ending_balance >0):
    month += 1
    starting_balance = ending_balance
    if starting_balance < payment:
        payment = starting_balance
    payment = pay
    middle_balance = starting_balance - payment
    interest = middle_balance * rate/12/100
    ending_balance = middle_balance + interest
    print("%-5d%10.2f%10.2f%10.2f%10.2f%10.2f"%
          (month, starting_balance, payment, middle_balance, interest, ending_balance))