# Task 1: Input Length Validator Write a script that asks for and checks 
# the length of the user's first name and last name. 
# Both should be at least 2 characters long. If not, print an error message.


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")


if len(first_name) >= 2:
    print("The first name is valid (length is greater than or equal to 2).")
else:
    print("The first name is too short (less than 2 characters).")

if len(last_name) >= 2:
    print("The last name is valid (length is greater than or equal to 2).")
else:
    print("The last name is too short (less than 2 characters).")