# Given an integer n. Write a program to find the first prime number greater than n.

# Examples:

# Input: n = 15
# Output: 17
# Explanation: 17 is next prime number.
n = int(input())

n = n + 1

while True :
    for i in range(2,n) :
        if n % i == 0 :
            break 
    else :
        print(n)
        break

    n += 1
