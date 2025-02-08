x= int(input())
y= int(input())
operator = int(input("enter 1 / 2 / 3 \n"))

match operator:
    case 1 :
        print("Addition",x+y)
    case 2:
        print("Subtraction",x-y)
    case 3:
        print("Multiplication",x*y)
    case _ : 
        print("invalid input")
    

# Given two numbers a and b. You need to perform basic mathematical operations on them. You will be provided an integer named as operator.

# If the operator equals to 1 add a and b, then print the result.
# If the operator equals to 2 subtract b from a, then print the result.
# If the operator equals to 3 multiply a and b, then print the result.
# If the operator equals to any other number, print "Invalid Input"(without quotes).
# Note: Do not add a new line at the end.

# Examples:

# Input: a = 1, b = 2, operator = 3
# Output: 2
# Explanation: 1 * 2 = 2