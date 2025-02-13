# Given two number n1 and n2, n1 > n2. Find the differences between mathematical tables 
# of n1 and n2 and print in a single line.


n1 = int(input())
n2 = int(input())

for i in range(1,11) :
    res = n1 * i - n2 * i 
    print(res, end = " ")  # print the result of each iteration in a single line9

print("new method")

for i in range(1,11) :
    print( n1 * i - n2 * i , end =" ")