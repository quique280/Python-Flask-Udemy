# ========================== WHILE LOOP
number = 7

while True:
    user_input = input("Would yo like to play?(Y/n): ")
    if user_input == "n":
        break
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif number - user_number in (1, -1):
        print("You were off by one!!")
    else:
        print("You're wrong!")


# ==================================================== FOR LOOP
friends = ["Rolf", "Jen", "Bob", "Anne"]
for friend in friends:
    print(f"{friend} is my friend.")

for num in range(4):
    print(f"This is number {num}")

grades = [34, 75, 95, 100, 67]
total = 0  # or you can do sum(grades) and ignore the for loop
amount = len(grades)

for grade in grades:
    total += grade
print(total / amount)
