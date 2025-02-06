# You are given two integer variables x and y. You need to perform the following operations:

# p = x + y : Addition
# q = x - y : Subtraction
# r = x * y :Multiplication
# s = x / y : Division
# t = x % y : Modulo
# Examples:

# Input: x = 1, y = 2
# Output: 3 -1 2 0 1 
# Explanation: The given operations are performed.


a = int(input())
b = int(input())

p = a + b
q = a - b
r = a * b
s = a / b
u = a//b
t = a % b
print(f" addition {p} \n subtraction {q} \n multiply {r} \n divide {s} \n floor division {u}\n modulos {t}")

# output
# 11
# 3
# addition 14
# subtraction 8
# multiply 33
# divide 3.6666666666666665
# floor division 3
# modulos 2