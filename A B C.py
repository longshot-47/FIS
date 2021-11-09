A = input("number of A: ")
B = input("number of B: ")
C = input("number of C: ")
largest = A
smallest = B
if B > largest:
    largest = B
elif C > B > largest and C > largest > B:
    largest = C
if A < smallest:
    smallest = A
elif C < smallest and C < A < smallest:
    smallest = C
print("the largest number is: "+largest)
print("the smallest number is: "+smallest)