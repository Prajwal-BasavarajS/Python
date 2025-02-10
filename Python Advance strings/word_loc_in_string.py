s= 'geeksforgeeks is best for geeks'
w= 'best'

pos = s.find(w)

# If word is found, calculate its position
if pos == -1:
    res = -1  # Word not found
else:
    res = s[:pos].count(' ') + 1  # Count spaces before the word and add 1

print(res)


a = 'geeksforgeeks is best for geeks'  # String
w = 'best'  # Target word

# Splitting `s` into a list of words
b = a.split()

# Initializing the result variable
res = -1

for i, word in enumerate(b):  # 'i' is the index, 'word' is the current word in the list
    if word == w: 
        res = i + 1  
        break  # Stop the loop once the word is found
        
print(str(res))
