'''
created by Ng Yat Lung
12-11-2021

1. input the number 
   Read(NUM)

2. determine that the NUM is prime or has divisors other than 1 
   2.1 determine if number is divisible by 2
       If NUM = 2                       
       Then NUM is a prime number
       Else If NUM is even
            Then NUM is not a prime number and halt
            Else 2.11  determine if (NUM divisible by odd integers >= 3 and  <=  (square root of NUM))
                       For LOOP := 3 to sqrt(NUM) by 2
                       Do If (NUM mod LOOP) = 0
                          Then NUM is not a prime number and halt

3. if we get here, print a message that NUM is a prime number 
   Write(NUM,"is a prime number");

4. finished
   Halt
   
'''
import math

number = int(input("input the number: "))

if number == 2:
    print(number,"is a prime number")
else:
    if number % 2 == 0:
        print(number,"is not a prime number")
    else:
        isPrime = True
        for i in range(3,round(math.sqrt(number)+1),2):
            if number % i == 0:
                print(number,"is not a prime number")
                isPrime = False
                break
        if isPrime:
            print(number, "is a prime number")