from dataclasses import dataclass

@dataclass
class Student:
    student_name = str
    student_id = str
    student_gpa = float

# The function that concatinated the variable 
def __str__(self ):
    return  f'Name: {self.name} StarID: {self.school_id} GPA: {self.gpa}' 

def main():

    student_name = input('Enter the student name? ')
    student_id = input(f'Enter {student_name} student Id! ' )
    student_gpa = input(f'Enter {student_name} student gpa! ')



    print(f'Name: {student_name}')
    print(f'ID: {student_id}')
    print(f'GPA: {student_gpa}')


main()

