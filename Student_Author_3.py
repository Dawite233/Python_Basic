from dataclasses import dataclass

@dataclass

class Student:
    def __init__(self, name, school_id, gpa):
        self.name = name
        self.school_id = school_id
        self.gpa = gpa


Dawite = Student('Dawit', 'ze5454fd', 3.7)
print(Dawite.name)
print(Dawite.school_id)
print(Dawite.gpa)


Dawite = Student

Dawite = Student('Dav', 'fsteet', 4.0)