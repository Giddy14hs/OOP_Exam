class Student:
    def __init__(self, studentID, name):
        self.studentID = studentID
        self.name = name
        self.subjects = {}

    def add_marks(self, subject, marks):
        self.subjects[subject] = marks

    def calculate_average(self):
        if self.subjects:
            return sum(self.subjects.values()) / len(self.subjects)
        return 0

    def display_grades(self):
        average = self.calculate_average()
        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 70:
            grade = "C"
        elif average >= 60:
            grade = "D"
        else:
            grade = "F"
        print(f"Student: {self.name}, Average: {average:.2f}, Grade: {grade}")

# Example usage
student = Student(101, "Alice")
student.add_marks("Math", 85)
student.add_marks("English", 78)
student.add_marks("Science", 92)
student.display_grades()
