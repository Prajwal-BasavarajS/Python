# Given two numbers a and b, you need to swap their values so a holds the value of b and b holds the value of a. Just write the code to swap values of a and b at the specified place.

a = int(input())
b = int(input())
print("a = " ,a)
print("b = " ,b)
# Here we are using a temporary variable to swap the values of a and b.

# temp = a
# a = b
# b = temp

# OR

a , b = b , a

# a = b 
# b = a     THIS METHOD IS WRONG IT WON'T WORK

print("\n a = ", a)
print("b = ", b)

