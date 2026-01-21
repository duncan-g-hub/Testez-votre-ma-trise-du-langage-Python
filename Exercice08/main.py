def log_decorator(func):
    def wrapper():
        print("Premier message")
        result = func()
        print("Second message")
        return result
    return wrapper

 
@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")

function_test()
