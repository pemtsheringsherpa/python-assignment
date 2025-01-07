class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and I am a {self.gender}.")

class Employee(Person):
    def __init__(self, name, age, gender, job_title):
        super().__init__(name, age, gender)
        self.job_title = job_title

    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, I am a {self.gender}, and I work as a {self.job_title}.")

# Example 
person = Person("pem tshering sherpa", 20, "male")
person.introduce()

employee = Employee("Bob", 40, "male", "engineer")
employee.introduce()