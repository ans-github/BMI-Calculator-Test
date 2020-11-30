#Functions
def menu_message():
    menu_message = """ Thank you for using this app, please select from options:
    [1] Input Weight
    [2] Print History
    [3] BMI Classification
    [4] Exit Application
    """
    print(menu_message)

#input function
def input_func():
    int(input("Please enter your input: "))

#Exit application

def exit_the_program():
    print("Thank you for using my BMI Calculator, application will now close...")