# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Mariam Assaad,11/20/2024,Created Script
#   <Your Name Here>,<Date>, <Activity>
# ------------------------------------------------------------------------------------------ #

import json

# Constants
MENU: str = '''---- Course Registration Program ----
Select from the following menu:  
  1. Register a Student for a Course
  2. Show current data  
  3. Save data to a file
  4. Exit the program
----------------------------------------- '''



FILE_NAME: str = "Enrollments.json"

# Variables
menu_choice: str = ""
students: list = []

# Classes
class FileProcessor:
    """Processes data to and from a file"""

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """Reads data from a file and loads it into a list of Student objects"""
        try:
            with open(file_name, "r") as file:
                list_of_dict_data = json.load(file)
                for student in list_of_dict_data:
                    student_object = Student(
                        first_name=student["FirstName"],
                        last_name=student["LastName"],
                        course_name=student["CourseName"],
                    )
                    student_data.append(student_object)
        except FileNotFoundError as e:
            IO.output_error_messages("The file does not exist. Starting with an empty list.", e)
        except json.JSONDecodeError as e:
            IO.output_error_messages("Error decoding JSON. Starting with an empty list.", e)
        except Exception as e:
            IO.output_error_messages("An unexpected error occurred while reading the file.", e)

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """Writes the list of Student objects to a JSON file"""
        try:
            list_of_dict_data = [
                {"FirstName": student.first_name, "LastName": student.last_name, "CourseName": student.course_name}
                for student in student_data
            ]
            with open(file_name, "w") as file:
                json.dump(list_of_dict_data, file, indent=4)
                print("Data successfully saved to file.")
        except Exception as e:
            IO.output_error_messages("An unexpected error occurred while saving to the file.", e)


class IO:
    """Handles input and output operations"""

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """Displays error messages with optional exception details"""
        print(f"Error: {message}")
        if error:
            print(f"-- Technical Details: {error} --")

    @staticmethod
    def output_menu(menu: str):
        """Displays the program menu"""
        print(menu)

    @staticmethod
    def input_menu_choice() -> str:
        """Prompts the user to select a menu option"""
        return input("Please select a menu option (1-4): ")

    @staticmethod
    def output_student_courses(student_data: list):
        """Displays all student data"""
        if student_data:
            print("Current Student Data:")
            for student in student_data:
                print(f"{student.first_name} {student.last_name} is registered for {student.course_name}.")
        else:
            print("No student data available.")

    @staticmethod
    def input_student_data(student_data: list):
        """Prompts the user to input a student's details and adds it to the list"""
        try:
            first_name = input("Enter the student's first name: ")
            if not first_name.isalpha():
                raise ValueError("First name should only contain letters.")
            last_name = input("Enter the student's last name: ")
            if not last_name.isalpha():
                raise ValueError("Last name should only contain letters.")
            course_name = input("Enter the course name: ")
            student_data.append(Student(first_name, last_name, course_name))
            print(f"{first_name} {last_name} registered for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("Input validation error.", e)
        except Exception as e:
            IO.output_error_messages("An unexpected error occurred.", e)


class Person:
    """A class representing a person"""

    def __init__(self, first_name: str = "", last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("First name must contain only alphabetic characters.")

    @property
    def last_name(self):
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("Last name must contain only alphabetic characters.")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(Person):
    """A class representing a student"""

    def __init__(self, first_name: str = "", last_name: str = "", course_name: str = ""):
        super().__init__(first_name, last_name)
        self.course_name = course_name

    @property
    def course_name(self):
        return self.__course_name

    @course_name.setter
    def course_name(self, value: str):
        if value:
            self.__course_name = value
        else:
            raise ValueError("Course name cannot be empty.")

    def __str__(self):
        return f"{super().__str__()} registered for {self.course_name}"


# Main Program
if __name__ == "__main__":
    FileProcessor.read_data_from_file(FILE_NAME, students)

    while True:
        IO.output_menu(MENU)
        menu_choice = IO.input_menu_choice()

        if menu_choice == "1":
            IO.input_student_data(students)
        elif menu_choice == "2":
            IO.output_student_courses(students)
        elif menu_choice == "3":
            FileProcessor.write_data_to_file(FILE_NAME, students)
        elif menu_choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please select 1, 2, 3, or 4.")

        print("\n")

print("Program Ended")