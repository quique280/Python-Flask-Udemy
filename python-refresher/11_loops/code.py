movies_watched = ["The matrix","Green Book","Her"]
user_movie = input("Enter something you've watched recently: ")

if user_movie in movies_watched:
    print(f"I've watch {user_movie} too!")
else:
    print("I haven't watch that yet.")



#=====================================================
number = 7
user_input = input("Enter 'y' if you'd like to play:")

if user_input in ("y","Y"):
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif number - user_number in (1,-1):
        print("You were off by one!!")
    else:
        print("You're wrong!")