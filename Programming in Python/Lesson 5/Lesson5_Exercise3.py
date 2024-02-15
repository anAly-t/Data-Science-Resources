class Student:
    def __init__(self, student_id, name, grades=[]):
        """
        Initialize a Student with student ID, name, and a list of grades.
        """
        self.student_id = student_id
        self.name = name
        self.grades = grades

    def add_grade(self, grade):
        """
        Add a grade to the student's list of grades.
        """
        self.grades.append(grade)
        print(f"Added grade {grade} for {self.name}.")

    def calculate_average_grade(self):
        """
        Calculate the average grade of the student.
        """
        if not self.grades:
            return 0  # Return 0 if no grades are available
        average_grade = sum(self.grades) / len(self.grades)
        return average_grade

    def display_student_info(self):
        """
        Display information about the student, including student ID, name, and average grade.
        """
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grades: {', '.join(map(str, self.grades))}")
        print(f"Average Grade: {self.calculate_average_grade()}")

# Creating instances of the Student class for different students
student1 = Student(student_id=101, name="Alice", grades=[85, 90, 92])
student2 = Student(student_id=102, name="Bob", grades=[78, 85, 80, 88])
student3 = Student(student_id=103, name="Charlie")

# Testing the methods
student1.display_student_info()
student1.add_grade(88)
student1.display_student_info()

student2.display_student_info()
student2.add_grade(92)
student2.display_student_info()

student3.display_student_info()

# In this code:

# The Student class represents a student with attributes such as student ID, name, and a list of grades.
# The add_grade method allows adding a grade to the student's list of grades.
# The calculate_average_grade method calculates the average grade of the student.
# The display_student_info method displays information about the student, including student ID, name, grades, and average grade.
# Instances of the Student class are created for different students (student1, student2, and student3).
# The display_student_info method is used to display information about each student.
# The add_grade method is used to add a new grade for one of the students, and the updated information is displayed again.