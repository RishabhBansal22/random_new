def print_num(n):
    if n == 0:
        return
    print_num(n-1)
    print(n)


def print_num_tree(n, depth=0):
    print(" | " * depth + f"print_num({n})")
    if n == 0:
        return 
    print(n)
    print_num_tree(n-1, depth+1)
    print(n)

# print_num(4)
# print_num_tree(4)



def factorial(n:int) -> int:
    "return the factorial of n using iteration"
    if n == 0 or n == 1:
        return 1
    num = 1
    while n >=1:
        num *= n
        n-=1
    return num

def factorial_rec(n:int) -> int:
    "return the factorial of n using recursion"
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n-1)


def factorial_rec_tree(n:int, depth= 0) -> int:
    "return the factorial of n using recursion and prints recursion tree"
    print(" | " * depth + f"factorial_tree({n})")
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec_tree(n-1, depth+1)

print(factorial_rec_tree(3))



#Fibonacci series
# fib = [0,1,1,2,3,5,8,13]
#in fibonacci each number is sum of two previous numbers

def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib(n-1)+fib(n-2)


def fib_tree(n:int, depth=0) -> int:

    "returns output along with the call stack tree"

    print(" | " * depth + f"fib({n})")
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib_tree(n-1, depth+1) + fib_tree(n-2, depth+1)


#print(fib(5))
# print(fib_tree(5))









    

