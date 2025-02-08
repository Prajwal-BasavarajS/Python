x= int(input())
y= int(input())
z = int(input("enter 1 / 2 / 3 \n"))

match z:
    case 1 :
        print("Addition",x+y)
    case 2:
        print("Subtraction",x-y)
    case 3:
        print("Multiplication",x*y)
    case _ : 
        print("invalid input")
    