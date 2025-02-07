# You are given a number N, you need to print its multiplication table.

# Note: Please go through the range function to understand why it's useful in for loops.

# Example 1:

# Input:
# N = 5
# Output:
# 5 10 15 20 25 30 35 40 45 50

n = int(input())
for i in range(1,11):
    print( n*i ,end = " ")


# print odd numbers for given n numbers using for Loop 

m = int(input())
for i in range(1,m+1,2) :
    print(i,end = " ")

# print even numbers for given n numbers using for Loop

j = int(input())
for j in range(2,j+1,2):
    print(j , end = " ")