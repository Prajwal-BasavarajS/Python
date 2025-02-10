s = "aaabbccaaaa"

# Initialize result list
res = []
count = 1

# Iterate through the string to count consecutive characters
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        res.append(s[i - 1] * count)
        count = 1
res.append(s[-1] * count)  # Append last group
print(res)  
