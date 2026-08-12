def calculate(operation, *nums):
    # operation -> sum, max, min
    if not nums:
        return None

    if operation == "sum":
        return sum(nums)
    elif operation == "max":
        return max(nums)
    elif operation == "min":
        return min(nums)
    else:
        print("unsupported operation")
        return None

#print(calculate("max", 1,2,3,4))

def create_profile(name, **details):
    print(f"{name}: {details}")
#create_profile("Hakan", age=23, height="1.81", weight="84kg")


def log_call(func, *args, **kwargs):
    print(f"Calling: {func.__name__}")
    result = func(*args, **kwargs)
    print(f"Result: {result}")
    return result

log_call(create_profile, "hakan", age=22, height=1.81)
log_call(calculate,"max",4,5,6)

nums = [5,3,9]
opts = {"reverse":True}
print(sorted(nums,**opts))

def unique_items(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            result.append(item)
        seen.add(item)
    return result

nums = [3,1,3,2,1,4]
print(unique_items(nums))