def validate_args(func):
    def wrapper(*arg):
        if len(arg) < 1:
            return "Not enough arguments"
        elif len(arg) > 1:
            return "Too many arguments"
        elif  type(arg[0]) is not int:
            return "Wrong types"
        elif arg[0] < 0:
            return "Negative argument"
        return func(*arg)
    return wrapper

@validate_args
def func(n): return n
print(func())
print(func(1, 2))
print(func("python killed me"))
print(func(-1))
print(func(1))