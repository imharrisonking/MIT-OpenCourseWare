# Fibonacci numbers using memoisation through a dictionary to store values already seen and look these up instead of recomputing

def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d)+fib_efficient(n-2, d)
        d[n] = ans
        return ans
        
d = {1:1, 2:2}

argToUse = 34

print(fib_efficient(argToUse, d))