name = "Bob"
greeting = "Hello, Bob"

print(greeting)

name = "Rolf"

print(greeting)

###############################################################
print('###############################################################')
###############################################################

name = "Bob"
greeting = f"Hello, {name}"

print(greeting)

name="Rolf"

print(greeting)

##############################################################
print('###############################################################')
##############################################################

name = "Bob"

print(f"Hello, {name}")

name="Rolf"

print(f"Hello, {name}")

##############################################################
print('###############################################################')
##############################################################

name = "Bob"
greeting = "Hello , {}"

with_name = greeting.format(name)
with_name_two = greeting.format("Rolf")

print(with_name)
print(with_name_two)