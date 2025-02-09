s = "hello"
# Calculate the middle index of the string
i = len(s) // 2

# Convert the first half to uppercase and concatenate with the second half
res = s[:i].upper() + s[i:]
print(res) 
