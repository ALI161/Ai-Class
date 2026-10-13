
class Student:
    def __init__(self, name, student_id, major):
        self.name = name
        self.student_id = student_id
        self.major = major

    def set_info(self, name, student_id, major):
        self.name = name
        self.student_id = student_id
        self.major = major

    def display_info(self):
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Major:", self.major)
        print("--------------------")

student1 = Student("Ali", 101, "Computer Science")
student2 = Student("Reza", 102, "Software Engineering")

student1.display_info()
student2.display_info()
