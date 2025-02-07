# Given three positive integers a, b and c. Your task is to perform some bitwise operations on them as given below:
# 1. d = a ^ a
# 2. e = c ^ b
# 3. f = a & b
# 4. g = c | (a ^ a)
# 5. e = ~ e
# Note: ^ is for xor.
# Then print d e f g space seperately. Move the cursor to the next line after printing.

# Examples:

# Input: a = 1, b = 2, c = 3
# Output: 0 -2 0 3
# Explanation: We print d e f g after performing the given operations.


a = input()
b = input() 
c = input()
d = a ^ a
e = c ^ b
f = a & b
g = c | (a ^ a)
e = ~e
print(d, e, f, g)  