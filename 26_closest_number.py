# Given two integers n and m. The problem is to find the number closest to n and divisible by m. If there is more than one such number, then output the one having the maximum absolute value.

# Examples :

# Input: n = 13 , m = 4
# Output: 12
# Explanation: 12 is the Closest Number to 13 which is divisible by 4.
# Input: n = -15 , m = 6
# Output: -18
# Explanation: -12 and -18 are both similarly close to -15 and divisible by 6. but -18 has the maximum absolute value. So, Output is -18

n = int(input())
m = int(input())

remainder = n % m 

if remainder == 0 :
    print(n)
else :
    lower_number = n - remainder 
    upper_number = n + remainder

    if (abs(lower_number-n) < abs(upper_number - n)):
        print(lower_number)
    elif abs(lower_number-n) > abs(upper_number - n):
        print(upper_number)
    else :
        print(lower_number if abs(lower_number) > abs(upper_number) else upper_number)