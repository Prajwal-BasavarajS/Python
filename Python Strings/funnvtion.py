def fun():
    return 

p = fun()
print(p)  # Output: None

for i in range(5):
    pass  # Placeholder for future code


def fun(n):
    return [n*2, n*3]

res = fun("hello")
print(res)  

def fun1(msg):
    def fun2():
        # Using the outer function's message
        return f"Message: {msg}"
    return fun2

# Getting the inner function
fun3 = fun1("Hello, World!")

# Calling the inner function
print(fun3())  
