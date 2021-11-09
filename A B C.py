A = input("number of A: ")
B = input("number of B: ")
C = input("number of C: ")
largest = A
if B > largest:
    largest = B
elif C > B > largest and C > largest > B:
    largest = C
print("the largest number is "+largest)
