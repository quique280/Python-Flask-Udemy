name = input('Enter your name: ')

print(name)

#############################################################

size_input = input('How big is you house (in square meters): ')
square_meters = int(size_input)
square_feet = square_meters * 10.8
print(f'{square_meters} square meters is {square_feet:.2f} square feet')