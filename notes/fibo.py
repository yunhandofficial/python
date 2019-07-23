def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def fib_loop(n):
    result = [1, 1,]
    for i in range(1, n):
        fib_sum = result[-1] + result[-2]
        result.append(fib_sum)
    return result[-1]