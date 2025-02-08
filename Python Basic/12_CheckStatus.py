# Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.

# Return True for the following cases:

# Either a or b (not both) is non-negative and the flag is false.
# Both a and b are negative and the flag is true.
# Otherwise, return False.

# Examples: 

# Input: a = 1, b = -1, flag = False
# Output: True
# Explanation: Since a is positive, b is negative, and flag is False, condition 1 holds true, so the function returns True.

a = int(input())
b = int(input())
if a>=1 and b>=1 :
    flag = "True"
else :
    flag = "False"

print(flag)