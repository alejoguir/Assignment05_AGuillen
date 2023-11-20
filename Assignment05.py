# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   AGuillen,11/13/2023,Created Script
#  # ------------------------------------------------------------------------------------------ #
import json
from json import JSONDecodeError

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
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"
# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict[str, str] = {}  # one row of student data
students: list[dict[str, str]] = []  # a table of student data
datamsg: str = ''   # Holds format data before to print
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# When the program starts, read the file data into a list of dictionary rows (table)
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    print('The file data was loaded successfully')
except FileNotFoundError as e:
    print("The file should exist before running this script!")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep="\n")
    print('Creating file if it does not exist')
    file = open(FILE_NAME,'w')
    json.dump(students, file)   # Loading initial data [] from collection students
except JSONDecodeError as e:
    print("The file is invalid")
    file = open(FILE_NAME, "w")
    json.dump(students, file)   # Loading initial data [] from collection students
except Exception as e:
    print('---Technical Information---')
    print(e, e.__doc__, type(e), sep="\n")
finally:
    if not file.closed:
        file.close()
# Present and Process the data
while True:
    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")
    # Input user data
    if menu_choice == "1":
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError('The first name must be alphabetic')
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError('The last name must be alphabetic')
            course_name = input("Please enter the name of the course: ")
            student_data = {'first_name': student_first_name, 'last_name': student_last_name, 'course_name': course_name}
            # Load it into the collection students (list)
            students.append(student_data)
        except ValueError as e:
            print(e)
            print('---Technical Information---')
            print(e.__doc__, type(e), sep='\n')
    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            student_first_name = student['first_name']
            student_last_name = student['last_name']
            course_name = student['course_name']
            datamsg = "The student {} {}, has been registered for {}"
            print(datamsg.format(student_first_name, student_last_name, course_name))
        print("-"*50)
    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students,file)
            file.close()
        except TypeError as e:
            print('---Technical Information---')
            print(e.__doc__, type(e), sep='\n')
        except Exception as e:
            print('---Technical Information---')
            print(e.__doc__, type(e), sep='\n')
        finally:
            if not file.closed:
                file.close()
    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")
print("Program Ended")
