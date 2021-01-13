from typing import List, Optional


class Student:
    def __init__(self, name: str, grades: List[int] = []):  # This is BAD!
        self.name = name
        self.grades = grades

    def take_exam(self, result):
        self.grades.append(result)


bob = Student("Bob")
bob.take_exam(90)
print(bob.grades)


rolf = Student("Rolf")
print(rolf.grades)


# =================================== This is why we dont use mutable variables as default parameters, so we should do this


class Student2:
    def __init__(self, name: str, grades: Optional[List[int]] = None):  # ignore this error
        self.name = name
        self.grades = grades or []

    def take_exam(self, result):
        self.grades.append(result)


bob = Student2("Bob")
bob.take_exam(90)
print(bob.grades)


rolf = Student2("Rolf")
print(rolf.grades)