from Functions.bmi_system import bmi_calc_imperial, bmi_calc_metric
from Functions.general_functions import exit_the_program, menu_message
from Functions.bmi_result import bmi_result

#Selection from menu
#need to set up a file system
def selection():
    inputting = int(input("Please enter your input: "))
    if inputting == int(1):
        selection_unit()
    elif inputting == int(2):
        print("this system still isn't set up")
    elif inputting == int(3):
        bmi_result()
        input("Please press any key to exit app..")
    elif inputting == int(4):
        exit_the_program()

#Selection of units
def selection_unit():
    print("Please enter 1 for Metric or 2 for imperial units")
    inputting = int(input("Please enter your input: "))
    if inputting == int(1):
        bmi_calc_metric()
    elif inputting == int(2):
        bmi_calc_imperial()