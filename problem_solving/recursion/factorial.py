def factorial(val):
    if val == 0 or val==1:
        return 1
    return val*factorial(val-1)
        
out = factorial(5)
print(out)
