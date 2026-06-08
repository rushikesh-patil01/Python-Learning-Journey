# Function as Argument
def greet(name):
    return f"Hello, {name}"

def loud(func):   # takes function as input
    def wrapper(name):
        return func(name).upper()
    return wrapper

shout = loud(greet)   # passing function
print(shout("Rushi"))   # HELLO, RUSHI


# Function Returning Function
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier   # returning a function

times3 = make_multiplier(3)
print(times3(5))   # 15