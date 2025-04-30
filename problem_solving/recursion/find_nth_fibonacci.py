def find_nth_fibonacci(n):
    if n <= 1:
        return 1
        
    return find_nth_fibonacci(n-1)+find_nth_fibonacci(n-2)
  
out = find_nth_fibonacci(5)  
print(out)
