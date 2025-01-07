class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")

    def is_passed(self):
        return self.marks >= 40

# Example 
student = Student("pem tshering sherpa", 23, 85)
student.display_details()
if student.is_passed():
    print("The student has passed.")
else:
    print("The student has not passed.")