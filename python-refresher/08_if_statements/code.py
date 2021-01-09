day_of_week = input("What day of the week is it today? ").lower()

if day_of_week == "monday":
    print("Have a great stat to your week!")  
elif day_of_week == "tuesday":
    print("It's tuesday!")
if day_of_week != "monday":
    print("Full speed ahead!")
else:
    print("My default case.")
print("This always run.")