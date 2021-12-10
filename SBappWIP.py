'''
Simple Billing System

Created on Oct 6, 2020

@author: tchan
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
        if transactionRecord[2] != 'C' and transactionRecord[2] != 'D':
            sys.stderr.write('\n' + 'Invalid transaction code: ' + '\n' + line)
        elif float(transactionRecord[3]) < 0:
            sys.stderr.write('\n' + 'Invalid transaction amt:' + '\n' + line)
        else:
            data.append(transactionRecord) # append each record to list data
        
def menuItem2():
    '''
    menuItem2() to print transaction data 
    '''
    print('%-20s%-30s%5s%10s'%('Name','Address','Txn', 'Amount'))
    print('='*65)

    # loop to print out each components
    for e in data:
        print('%-20s%-30s%5s%10s'%(e[0], e[1], e[2], e[3]))
        
def menuItem3():
    try:
        customerName = input("Customer name: ")
        transactionType = input("Transaction type (C/D): ")
        if transactionType != 'C' and transactionType != 'D':
            raise Exception ('Invalid Transaction Type')
        transactionAmt = float(input("Transaction amount: "))
        if transactionAmt < 0:
            raise Exception ('Invalid Transaction Amount')        
                
        i = 0
        while i < len(clientDataList) and clientDataList[i]['Name'] != customerName:
            i  += 1

        if i == len(clientDataList):
            raise Exception ('Invalid Customer Name')
        
        if transactionType == 'C':
            clientDataList[i]['Balance'] -= transactionAmt
        else:
            clientDataList[i]['Balance'] += transactionAmt
                    
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
    
def menuItem4():
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
        choice = input( "Enter 1 to 4 " ) 

        if choice == "1":
            displayFile(sys.argv[1])
        elif choice == "2":           
            menuItem2()
        elif choice == "3":
            menuItem3()        
        elif choice == "4":
            menuItem4()
        elif choice == "Q":
            break

    print ("End Simple Billing System")

if __name__ == "__main__":
    sys.argv = [sys.argv[0], 'datafile0.dat']
    
    displayFile(sys.argv[1])
    readData(sys.argv[1])
    creatCustomerList()
    main()