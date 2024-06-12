# classes_and_objects/classes_and_objects.py


# Define the Course class to represent a course
class Course:
    def __init__(self, title, instructor, duration):
        self.title = title  # Title of the course
        self.instructor = instructor  # Name of the instructor
        self.duration = duration  # Duration of the course in hours

    def get_details(self):
        # Return a string with the course details
        return f"{self.title} by {self.instructor} lasts for {self.duration} hours."


# Define the Student class to represent a student
class Student:
    def __init__(self, name):
        self.name = name  # Name of the student
        self.enrolled_courses = []  # List to store enrolled courses

    def enroll(self, course):
        # Add a course to the student's enrolled courses list
        self.enrolled_courses.append(course)

    def list_courses(self):
        # Return a list of details for each enrolled course
        return [course.get_details() for course in self.enrolled_courses]


# Example usage of the classes
if __name__ == "__main__":
    # Create instances of Course
    python_course = Course("Python Fundamentals", "John Doe", 40)
    java_course = Course("Java Basics", "Jane Smith", 30)

    # Create an instance of Student
    student = Student("Alice")

    # Enroll the student in courses
    student.enroll(python_course)
    student.enroll(java_course)

    # Print the courses the student is enrolled in
    print(f"{student.name} has enrolled in the following courses:")
    for course in student.list_courses():
        print(course)
