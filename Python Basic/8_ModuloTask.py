# Given an integer N. FInd an integer K for which N%K is the largest ( 1 <= K < N).

 

# Example 1:

# Input:
# N = 3
# Output:
# 2
# Explanation:
# 3%1 = 0
# 3%2 = 1
# So, the modulo is highest for 2.

n = int(input())
print(n-1)  # This will print the largest possible value of K for which N%

def find_max_modulo(N):
    if N <= 1:
        return None  # No valid K for N <= 1
    return (N // 2) + 1

# Example Input
N = 6
print(find_max_modulo(N))  # Output: 2
