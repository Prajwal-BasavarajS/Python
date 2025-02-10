s = 'geeksforgeeks is best'

# Initializing mapping dictionary
d = {'e': '1', 'b': '6', 'i': '4'}

# Using translate() with maketrans()
res = s.translate(str.maketrans(d))

print(res)
