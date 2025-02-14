# Given an integer n check if n is prime or not.
# A prime number is a number that is divisible by 1 and itself only.

# Note: Print "True" if n is prime, otherwise print "False".

# Examples:

# Input: n = 17
# Output: True 
# Explanation: 17 is  divisible by only 1 and 17. So it's a prime number.


n = int(input())

# for i in range( 1 , n+1) :
#     if n % i == 0 :
#         if i == 1 and i == n :
#             print("True")
#         else :
#             print("False")

isPrime = True

if n <= 1 :
    isPrime = False

for i in range(2,n) :
    if n % i == 0 :
        isPrime = False

print(isPrime)
