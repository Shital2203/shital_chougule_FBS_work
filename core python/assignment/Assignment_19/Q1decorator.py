def memoization(func):
    cache = {}
    def wrapper(n):
        if n in cache:
            print("output from cache")
            return cache[n]
        result = func(n)
        cache[n] = result
        print("output not avalaible in cache")
        return result
    return wrapper
@memoization
def fibonacci(n):
    f=1
    for i in range(1,n+1):
        f+=1
    return f



