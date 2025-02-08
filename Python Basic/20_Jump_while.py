x = int(input())
start = 1
jump = 1

while(jump <= x):
    print(jump, end = " ")
    start += 1
    jump = start**2
    #(1**1) 2**2 = 4  3**3 = 9 4**4 = 16
    
    # if(jump > x):
    #     break
