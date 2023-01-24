from dataclasses import dataclass

@dataclass

class Student:
    name: str
    school_id: str



Dawite = Student('Dawit', 'ze5454fd')
print(Dawite.name)
print(Dawite.school_id)


Dawite = Student

Dawite = Student('Dav', 'fsteet')