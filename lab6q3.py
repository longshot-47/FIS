'''
filename:loanTable.py
date:Nov 16
author:T. Chan
'''
try:
    loanAmount = int(input('The loan amount is :'))
    if loanAmount < 1000 or loanAmount > 100000:
        raise Exception ('Invalid Loan Amount')
    annualInterestRate = int(input('The annual interest rate is:'))
    if annualInterestRate < 0.1 or annualInterestRate > 100:
        raise Exception ('Invaild interset rate')
    monthlyPayment = int(input('The monthly payment is:'))
    if loanAmount * annualInterestRate/12/100 > monthlyPayment:
        raise Exception ('Invalid Monthly Payment - less the monthly interset')
    startingBalance = loanAmount
    payment = monthlyPayment
    middleBalance = startingBalance - payment
    interest = middleBalance * annualInterestRate/12/100
    endingBalance = middleBalance + interest
    month = 1

    print('''
                  Starting            Middle              Ending
    Month	Balance   Payment   Balance   Interest  Balance
    -------------------------------------------------------''')
    print("%-5d%10.2f%10.2f%10.2f%10.2f%10.2f"%
              (month,startingBalance,payment,middleBalance,interest,endingBalance))

    while (endingBalance > 0):
     
        startingBalance = endingBalance
        if endingBalance < payment:
            payment = endingBalance
        middleBalance = startingBalance - payment
        interest = middleBalance * annualInterestRate/12/100
        endingBalance = middleBalance + interest
        month += 1
    print("%-5d%10.2f%10.2f%10.2f%10.2f%10.2f"%
        (month,startingBalance,payment,middleBalance,interest,endingBalance))
    if month > 100:
        raise Exception ('Invalid Monthly Payment - more than 100 payment')
        
    
except Exception as exception:
    print(exception)