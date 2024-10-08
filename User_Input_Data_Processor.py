# Task 1: Input Length Validator Write a script that asks for and checks 
# the length of the user's first name and last name. 
# Both should be at least 2 characters long. If not, print an error message.

def check_name_length():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    
    print(f"Length of first name '{first_name}': {len(first_name)} characters.")

    
    print(f"Length of last name '{last_name}': {len(last_name)} characters.")


check_name_length()