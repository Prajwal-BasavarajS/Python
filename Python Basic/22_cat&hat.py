# You are given a string str, you need to return True if  the words "cat" and "hat" appear same number of times in str, otherwise return False.
# Note: str contains only lowercase English alphabets.

# Example 1:

# Input:
# str = catinahat
# Output:
# True
# Explanation:
# cat and hat both are present
# 1 number of times.

str = input()
cat = 0
hat = 0
for i in range(0, len(str)-2 , 1) :
    if(str[ i : i + 3 ] == 'cat' ) :
        cat+=1
    if(str[ i : i + 3 ] == 'hat' ) :
        hat+=1
if ( cat == hat ):
    print("True")
else: 
    print("False")
    
