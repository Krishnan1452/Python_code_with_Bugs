# A program to calculate and display student grades
class Student:
    def __init__(self, name, marks): 
        self.name = name
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks) 

    def assign_grade(self):
        avg = self.calculate_average
        if avg >= 90:   
            grade = "A"
        elif avg >= 75
            grade = "B"  
        elif avg >= 50:
            grade = "C"
        else:
            grade = "F"
        return grade

# Main program
def main():
    num_students = int(input("Enter number of students: ")) 
    students = []
    for i in range(num_students):
        name = input("Enter name of student: ")
        marks = input("Enter marks separated by commas: ").split(",") 
        students.append(Student(name, marks))

    print("Student Grades:")
    for student in students:
        grade = student.assign_grade()  
        print(f"Student: {student.name}, Grade: {grade}")

if __name__ == "__main__"
    main() 