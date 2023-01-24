from dataclasses import dataclass

@dataclass

class Student:
    name: str
    school_id: str
    gpa: float

    def __str__(self):
        return f'Name: {self.name} StarID: {self.school_id} GPA: {self.gpa}' 

def main():
    Dawite = Student('Dawit', 'ze5454fd', 3.8)
    print(Dawite.name)
    print(Dawite.school_id)
    print(Dawite.gpa)
    print(Dawite)


Elsa = Student('Elsa', 'fadfsa', 4.0)
print(Elsa)


if __name__ == "__main__":
    main()



