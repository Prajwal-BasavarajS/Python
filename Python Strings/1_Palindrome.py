str = input("Enter string for palindrome checking.. \n")

s1 = str[: : -1]

if s1 == str :
    print("The string is a palindrome")
else :
    print("The string is not a palindrome")




def is_symmetrical(s):
    length = len(s)
    mid = length // 2
    if len(s) % 2 == 0:
        s1 = s[:mid]
        s2 = s[mid:]
    else:
        s1 = s[:mid]
        s2 = s[mid + 1:]
    
    return s1 == s2

s = input("Enter string for symmetrical \n")
if is_symmetrical(s):
    print("Symmetrical")
else:
    print("Not Symmetrical")

