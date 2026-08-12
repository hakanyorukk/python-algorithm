import functools
import time


# def add_sprinkles(func):
#     def wrapper(*args, **kwargs):
#         print("*You add sprinkles 🎊 *")
#         func(*args, **kwargs)
#     return wrapper
#
# def add_fudge(func):
#     def wrapper(*args, **kwargs):
#         print("*You add fudge 🍫*")
#         func(*args, **kwargs)
#     return wrapper
#
# @add_sprinkles
# @add_fudge
# def get_ice_cream(flavor):
#     print(f"Here is your {flavor} ice cream 🍨")

# get_ice_cream("vanilla")

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"time takes: {end-start}")
        return result
    return wrapper

@timer
def sum_10_000_000():
    return sum(range(10_000_000))

#print(f"time takes for this function: {sum_10_000_000()}")

def logger(func):
    @functools.wraps(func)   # copies name, docstring etc...
    def wrapper(*args, **kwargs):
        print(func.__name__)
        print(f"args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@timer
@logger
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍨")

get_ice_cream("chocolate")

