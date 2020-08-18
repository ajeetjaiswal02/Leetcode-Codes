##def fib(n):
##    if n == 1 or n == 0:
##        result = 1
##    else:
##        result = fib(n-1) + fib(n-2)
##    return result

##print(fib(89))            

def drop(n):
    if n == 1 or n == 0:
        return 1
    value_no = [None] * (n+1)
    value_no[1] = 1
    value_no[2] = 2
    for i in range(3,n+1):
        value_no[i] = value_no[i-1] + value_no[i-2]
    return value_no[n]

print(drop(4))