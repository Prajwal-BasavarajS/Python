# Given a number n, find the sum of the first natural numbers.

# Examples : 

# Input: n = 3
# Output: 6
# Explanation: Note that 1 + 2 + 3 = 6

n = int(input())
sum = 0
for i in range(1,n+1):
    sum += i
print(sum)