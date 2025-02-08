

year = int(input())
isLeap = False

if year % 4 == 0 and year % 100 != 0:

    isLeap = True

elif year % 400 == 0:

    isLeap = True

else:
    isLeap = False

print(isLeap)