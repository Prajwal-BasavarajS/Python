# Given an integer n. Write a program to print all the divisors of n in a single line.

# Examples:

# Input: n = 12
# Output: 1 2 3 4 6 12
# Explanation: 12 is divisible by 1 2 3 4 6 12.

n = int(input())

for i in range (1, n+1) : 
    if n % i == 0 :
        print(i, end = " ")  # print the divisor and a space after it