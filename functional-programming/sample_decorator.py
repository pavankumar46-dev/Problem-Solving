def sample_decorator(func):
    def wrapper():
        print("Going to decorate")
        func()
        print("Successfully decorated")
        
    return wrapper
    
@sample_decorator
def print_val():
    print("Normal Function")

print_val()
