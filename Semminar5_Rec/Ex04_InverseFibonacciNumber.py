def fib(n):
    if n > 0:
        if n in [1,2]:
            return 1
        return fib(n-1) + fib(n-2)
    else:
        if n in [-1]:
            return 1
        return fib(n+2) - fib(n+1)

list = []
for i in range(-10,10):
    list.append(fib(i))
print(list)