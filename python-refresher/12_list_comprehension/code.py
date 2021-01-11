numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers]

# Other languages way
# for x in numbers:
#   doubled.append(x * 2)


# --------------------------------------------------
friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [
    f for f in friends if f.startswith("S")
]  # this two lists aren't the same list, but they have the same content

# Other languages way
# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)

print(starts_s)