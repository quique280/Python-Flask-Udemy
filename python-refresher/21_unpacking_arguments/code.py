def multiply2(*args):
    print(args)


multiply2(1, 3, 5)


def add(x, y):
    return x + y


nums = [5, 3]
print(add(*nums))


nums = {"x": 15, "y": 25}
print(add(**nums))


# =============================================


def multiply(*args):
    total = 1
    for arg in args:
        total *= arg
    return total


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()"


print(apply(1, 23, 214, 4324, 324, operator="*"))
print(apply(1, 23, 214, 4324, 324, operator="+"))
