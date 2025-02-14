# Given an integer n find the sum of the first n natural number.

# Examples:

# Input: n = 10
# Output: 55
# Explanation: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55.



x = int(input())
sum = 0
for i in range(x+1) :
    sum = sum + i

print(sum)