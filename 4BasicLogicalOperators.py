# Logical operators and, or, not are used in condition checking. Like a and b checks if both a and b are True. 
# First a is checked then b is checked. a or b checks if either of a or b is True. If one is True;
# it doesn't check for the other. not a complements the boolean value of a.
# Note: 0 and empty string are False and all other values are True.
# In this question you basically need to do
# a and b
# a or b
# not a

# Input: a = 0, b = 2
# Output: 0 2 True
# Explanation: 0 and 2 gives 0. 0 or 2 gives 2. not 0 give True as 0 is False.

a = int(input())
b = int(input())

print(f"AND =  {a and b}")

print(f"OR = {a or b}")  

print(f"Not = {not a}")   

# AND understanding
#if a=0(false) b = 3/5/66 anything (its true) 0|1 = 1 is OR condition so ans is (b)
#if a = 9 and b = 8 then ans =9 greater value contains more number of true values so it gets printed

# OR understanding
#if a = 1 (its true) so ans/ output wld be false   
# if a=3 as all values of integer except 0 are true so ans wld be false