# Input string
s = "hello world hello everyone"

# Initialize an empty dictionary to store word frequencies
w_freq = {}

# Calculate word frequencies using a for loop
for word in s.split():
    w_freq[word] = w_freq.get(word, 0) + 1

# Print the result
print(w_freq)
