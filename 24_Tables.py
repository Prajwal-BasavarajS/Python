# Create the multiplication table of a given number N and return the table as an array


x = int(input())

for i in range(1,11):
    print(f'{x} x {i} = {x * i}')

# 9 X 1 = 9
# 9 x 2 = 18
# 9 x 3 = 27
# 9 x 4 = 36
# 9 x 5 = 45
# 9 x 6 = 54
# 9 x 7 = 63
# 9 x 8 = 72
# 9 x 9 = 81
# 9 x 10 = 90

y = int(input("input for y"))

for i in range(1,11):
    print( y * i , end = " ")

# 5 10 15 20 25 30 35 40 45 50

