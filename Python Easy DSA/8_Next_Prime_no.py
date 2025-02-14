# Given an integer n. Write a program to find the first prime number greater than n.

# Examples:

# Input: n = 15
# Output: 17
# Explanation: 17 is next prime number.
n = int(input())      #11

n = n + 1             #12

while True :
    for i in range(2,n) :    #(2,12) for loop till 11 => (2,3,4,5,6,7,8,9,10,11)
        if n % i == 0 :      #
            break 
    else :
        print(n)
        break

    n += 1
