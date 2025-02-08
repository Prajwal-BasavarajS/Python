# Given an integer n. Write a program to print the last digit of the number. Also, move the cursor to the next line.

# Examples:

# Input: n = 10
# Output: 0
# Input: n = 9768
# Output: 8


N = int(input()) 
res = abs(N) % 10 # modulus give the last digit or remainder when divided by 10
print(res)
