'''
Simple Billing System

Created on Oct 13, 2021

@author: Ng Yat Lung(57170429)
'''
import fileinput
import sys

data=[]
clientDataList = []

def displayFile(datafile):
    for line in fileinput.input(datafile):
        sys.stdout.write(line)
        
def readData(datafile):
    '''
    readData() to read in transaction data and store in a list
    '''
    fileIn = open(datafile, 'r') # open inputfile using paramepasster datafile

    lines = fileIn.read().splitlines() # read in all transaction lines

    for line in lines:
        transactionRecord = line.split('_') # convert line to record
        if len(transactionRecord) == 4:
            if transactionRecord[2] != 'C' and transactionRecord[2] != 'D':
                sys.stderr.write('\n' + 'Invalid transaction code: ' + '\n' + line) # detect and show error on transaction code
            if float(transactionRecord[3]) < 0:
                sys.stderr.write('\n' + 'Invalid transaction amt:' + '\n' + line) # detect and show error on transaction amount
            else:
                data.append(transactionRecord) # append each record to list data
        else:
            sys.stderr.write('\n' + 'Invalid data format: '+ '\n' + line + '\n' + 'Acceptable data format: ' + '\n' + 'Name_Address_Transcation code_transaction amount')     
def show_trans_data():
    '''
    menuItem2() to print transaction data 
    '''
    print('%-20s%-30s%5s%10s'%('Name','Address','Txn', 'Amount'))
    print('='*65)

    # loop to print out each components
    for e in data:
        print('%-20s%-30s%5s%10s'%(e[0], e[1], e[2], e[3]))
        
def input_trans_data():
    try:
        sys.stderr.write('Input Q to exit'+'\n')
        customerName = input("Customer name: ")
        if customerName == 'Q':
            sys.stderr.write('Back to main menu')
            main()
        transactionType = input("Transaction type (C/D): ")
        if transactionType == 'Q':
            sys.stderr.write('Back to main menu')
            main()
        elif transactionType != 'C' and transactionType != 'D':
            raise Exception ('Invalid Transaction Type') # detect and show error on transaction code
        transactionAmt = float(input("Transaction amount: "))
        if transactionAmt < 0:
            raise Exception ('Invalid Transaction Amount') # detect and show error on transaction amount
                
        i = 0
        while i < len(clientDataList) and clientDataList[i]['Name'] != customerName:
            i  += 1 # loop to print transaction record

        if i == len(clientDataList):
            raise Exception ('Invalid Customer Name') # detect and show error on customer name
        
        if transactionType == 'C':
            clientDataList[i]['Balance'] -= transactionAmt
        else:
            clientDataList[i]['Balance'] += transactionAmt # adjust transaction amount
                    
        print('%-20s%-30s%10s'%('Name','Address','Balance'))
        print('%-20s%-30s%9s'%('-'*4 , '-'*7 , '-'*6))
                
        for e in sorted(clientDataList, key = lambda c: c['Name']):
            if e['Balance'] != 0:
                print('%-20s%-30s%10.2f'%(e['Name'], e['Address'], e['Balance']))
                

    except Exception as exception:
        sys.stderr.write(str(exception)+'\n')

def creatCustomerList():
        for e in data:     
            if len(clientDataList) == 0:
                if e[2] == 'C':
                    clientDataList.append(dict(zip(['Name','Address','Balance'],
                                                    [e[0], e[1], -float(e[3])])))
                else:
                    clientDataList.append(dict(zip(['Name','Address','Balance'],
                                                    [e[0], e[1], float(e[3])])))
            else:
                i = 0
                while i < len(clientDataList) and clientDataList[i]['Name'] != e[0]:
                    i  += 1

                if i == len(clientDataList):
                    if e[2] == 'C':
                        clientDataList.append(dict(zip(['Name','Address','Balance'],
                                                        [e[0], e[1], -float(e[3])])))
                    else:
                        clientDataList.append(dict(zip(['Name','Address','Balance'],
                                                        [e[0], e[1], float(e[3])])))
                else:
                    if e[2] == 'C':
                        clientDataList[i]['Balance'] -= float(e[3])
                    else:
                        clientDataList[i]['Balance'] += float(e[3])      
    
def show_report():
    '''
    to print customer report
    '''         
    print('%-20s%-30s%10s'%('Name','Address','Balance'))
    print('%-20s%-30s%9s'%('-'*4 , '-'*7 , '-'*6))
            
    for e in sorted(clientDataList, key = lambda c: c['Name']):
        if e['Balance'] != 0:
            print('%-20s%-30s%10.2f'%(e['Name'],e['Address'],e['Balance'])) 

def main():
    instructions = """\nEnter one of the following:
        1 to print the contents of input transaction file
        2 to print all valid input transaction data
        3 to enter adjustment transaction
        4 to print customer report
        Q to end \n"""
    
       
    while True:
        sys.stdout.write(instructions) 
        sys.stdout.flush()      
        choice = input( "Enter 1 to 4 or Q " ) 

        if choice == "1":
            displayFile(sys.argv[1])
        elif choice == "2":           
            show_trans_data()
        elif choice == "3":
            input_trans_data()        
        elif choice == "4":
            show_report()
        elif choice == "Q":
            break
        elif choice != "1" or "2" or "3" or "4" or "Q":
            sys.stderr.write('enter 1 to 4 or Q only' + '\n')

    print ("End Simple Billing System")

if __name__ == "__main__":
    sys.argv = [sys.argv[0], 'datafile0.dat']
    
    displayFile(sys.argv[1])
    readData(sys.argv[1])
    creatCustomerList()
    main()
