# Given three numbers a, b, and c. You need to find which is the greatest of them all.

a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print(f"Greatest is a = {a}")
elif b > a and b > c:
    print(f"Greatest is b = {b}")
else :
    print(f"Greatest is c = {c}")

