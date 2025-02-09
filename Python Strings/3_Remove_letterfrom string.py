s = "hello world"
print(s.split())  # ['hello', 'world']

s = s.replace('l',"")
print(s)  # "heo word"

# Same using loop

s1 = ""

for char in s:
    if char == 'l':
        s1 += " "
    else:
        s1 += char
    
print("\n", s1)  # "heo word"
