A = input("number of A")
B = input("number of B")
C = input("number of C")
largest = A
if B > largest:
    largest = B
elif C > largest:
    largest = C
print(largest)
