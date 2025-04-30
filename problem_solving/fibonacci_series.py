def fibonacci_series(n):
    a, b = 0, 1
    fib_series = []
    
    for _ in range(n):
        fib_series.append(a)
        
        a, b = b, a+b
        
    return fib_series
    
out = fibonacci_series(7)
print(out)
