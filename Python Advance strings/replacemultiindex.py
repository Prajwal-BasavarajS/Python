s = "geeksforgeeks is best"
li = [2, 4, 7, 10]  # Indices to replace
ch = '*'  # Replacement character

temp = list(s)
# Replace characters at specified indices
for i in li:
    temp[i] = ch

res = ''.join(temp)
print("The String after performing replace:", res)
