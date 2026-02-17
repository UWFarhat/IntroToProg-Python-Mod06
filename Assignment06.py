# ------------------------------------------------------------------------------------------ #
# Title: Assignment06.py
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   mofarhat, 2/16/2026, Created Script from Assignment06-Start.py
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
students: list = []  # a table of student data
menu_choice: str = ''  # Hold the choice made by the user.

class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    mofarhat, 2/16/2026 Created class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a json file into a list of dictionary rows

            ChangeLog: (Who, When, What)
            mofarhat, 2/16/2026, Created function

            :return: list
        """
        try:
            file = open(file_name, "r")
            new_data = json.load(file)
            for student in new_data:
                student_data.append(student)
            file.close()
            return student_data
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file into a list of dictionary rows

            ChangeLog: (Who, When, What)
            mofarhat, 2/16/2026, Created function
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file, indent=2)

            file.close()
            print("The following data was saved to file!")
            for student in student_data:
                print(f'{student["FirstName"]},{student["LastName"]},{student["CourseName"]}')
        except Exception as e:
            IO.output_error_messages("There was an error writing to file", e)
        finally:
            if file.closed == False:
                file.close()

class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
        mofarhat, 2/16/2026, Created Class
        mofarhat, 2/16/2026, Added output menu function
        mofarhat, 2/16/2026, Added output error messages function
    """

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        mofarhat, 2/16/2026, Created function

        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)     # Present the menu of choices
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error message to the user

        ChangeLog: (Who, When, What)
        mofarhat, 2/16/2026, Created function

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_student_courses(student_data: list):
        """ This function displays a string of comma-separated values for each row in the students variable.

        ChangeLog: (Who, When, What)
        mofarhat, 2/16/2026, Created function

        :return: None
        """
        print("-" * 50)
        if len(student_data) > 0:
            for student in student_data:
                print(f'{student["FirstName"]},{student["LastName"]},{student["CourseName"]}')
        else:
            print("No data to display.")
        print("-" * 50)

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        mofarhat, 2/16/2026, Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message
        return choice

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets input from the user on Student and Course names

        ChangeLog: (Who, When, What)
        mofarhat, 2/16/2026, Created function

        :return: none
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            new_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(new_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with your entered data.", e)
        return student_data

# Read the data from file, present the menu and process user input
FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)
while True:
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":
        IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")