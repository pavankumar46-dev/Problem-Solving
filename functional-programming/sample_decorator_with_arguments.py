def sample_decorator(func):
    def wrapper(a, b):
        print("Going to decorate")
        func(a, b)
        print("Successfully decorated")
        
    return wrapper
    

@sample_decorator
def print_val(a, b):
    print(a+b)
    
print_val(1, 2)
