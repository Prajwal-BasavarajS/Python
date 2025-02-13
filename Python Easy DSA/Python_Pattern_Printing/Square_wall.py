# Given an integer n,  write a program to print the square wall of size n using nested loops.
#  Try not to use String multiplication.

# Examples:

# Input: n = 5
# Output:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *


# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print("* ", end="")


print()

m = 3
for i in range(m) :
    print("* "*m)
