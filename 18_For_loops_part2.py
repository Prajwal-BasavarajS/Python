# You are given a string str, you need to print its characters at even indices(index starts at 0).

# Note: Please go through the range function to understand how to jump 2 steps.

# Example 1:

# Input:
# str = DoctorPhenomenal
# Output:
# DcoPeoea

str = input()
for i in range(0,len(str),2) :
    print(str[i], end="")