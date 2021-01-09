print(5 == 5 )
print(5 > 5)
print(10 != 10)

#comparisons: ==, !=, >, <, >=, <=


friends = ["Rolf","Bob"]
abroad = ["Rolf","Bob"]

print(friends == abroad)
print(friends is abroad) #checks if its in the same memory space, not is has the same elements
friends = abroad
print(friends is abroad) 