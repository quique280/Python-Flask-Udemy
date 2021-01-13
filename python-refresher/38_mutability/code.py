a = []

b = a

a.append(35)

print(a)
print(b)

print(id(a))
print(id(b))


# Lists are mutable, tuples, strings, integers are not