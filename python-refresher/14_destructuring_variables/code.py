x, y = 5, 11
t = 5, 11
x, y = t

print(x, y)

# =====================================================


student_attendance = {"Rolf": 96, "Adam": 80, "Anne": 100}
print(list(student_attendance.items()))

# for t in student_attendance.items():
#     print(t)
for x, y in student_attendance.items():
    print(x, y)

# ====================================================
people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for name, age, profession in people:
    print(f"Name:{name}, Age:{age}, Profession: {profession}")

# =====================================================================
person = ("Bob", 42, "Mechanic")
name, _, profession = person


# ==========================================
head, *tail = [1, 2, 3, 4, 5]
print(head, tail)

*head, tail = [1, 2, 3, 4, 5]
print(head, tail)
