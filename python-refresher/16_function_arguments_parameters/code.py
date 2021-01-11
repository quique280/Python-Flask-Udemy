def add(x, y):
    result = x + y
    print(result)
    return result


add(5, 3)

# ===============================================
def say_hello1(name, surname):
    print(f"Hello, {name} {surname}")


# positional arguments
say_hello1("Bob", "Smith")

# named or keyword argumengts
say_hello1(surname="Smith", name="Bob")


# ===============================================


def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You fool!")


divide(dividend=15, divisor=0)
divide(dividend=15, divisor=3)
