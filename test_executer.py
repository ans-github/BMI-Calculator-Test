import os

#My BMI Calculator 07/09/2021 - Goal 80kg
#This is still in progress and many tweaks are still needed. However it does perform the function.

#Functions required:
# Date Settings
# Clear Screen
# Unit Converter
# File Save System 
# GUI Needs setting up
# Return to menu system

#date section
# now = datetime.now()
# print("now.month, now.year, now.day, now.second, now.hour, now.minute")

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

#Clear Screen
def clear_screen():
    os.system("clear")

#Selection from menu
#need to set up a file system
def selection():
    inputting = int(input("Please enter your input: "))
    if inputting == int(1):
        selection_unit()
    elif inputting == int(2):
        print("this system still isn't set up")
        input("Please press any key to return to menu..")
        clear_screen()
        menu_message()
        selection()
    elif inputting == int(3):
        bmi_result()
        input("Please press any key to return to menu..")
        clear_screen()
        menu_message()
        selection()
    elif inputting == int(4):
        clear_screen()
        exit_the_program()

#Selection of units
def selection_unit():
    print("Please enter 1 for Metric or 2 for imperial units")
    inputting = int(input("Please enter your input: "))
    if inputting == int(1):
        clear_screen()
        bmi_calc_metric()
    elif inputting == int(2):
        clear_screen()
        bmi_calc_imperial()

#Selection after result
def selection_result():
    inputting = input("Would you like to compare your stats to our bmi chart? type yes or no: ")
    if inputting == "yes":
        bmi_result()
        input("Please press any key to return to menu..")
        menu_message()
        selection()
    elif inputting == "no":
        input("Please press any key to return to menu..")
        clear_screen()
        menu_message()
        selection()
    else:
        print("That is not a valid response, please try again")

#Calculations (metric and imperial)
def bmi_calc_metric():
    my_input = int(input("please enter your weight in KG: "))
    my_input2 = int(input("please enter your height in cm: "))
    bmi_result_met = my_input / my_input2 / my_input2 * 10000
    print("Your BMI is " + str(bmi_result_met))
    selection_result()

def bmi_calc_imperial():
    my_input = int(input("Please enter your weight in lbs: "))
    my_input2 = int(input("Please enter your height in inches: "))
    first_calc = my_input / my_input2
    second_calc = first_calc / my_input2
    third_calc = second_calc * 703
    print("Your BMI is " + str(third_calc))
    selection_result()

def bmi_result():
    print("""
    BMI of 15 = Very Severely Underweight
    BMI between 15 to 16 = Severely Underweight
    BMI between 16 to 18.5 = Underweight
    BMI between 18.5 to 25 = Normal (Healthy Weight)
    BMI between 25 to 30 = Overweight
    BMI between 30 to 35 = Moderately Obese
    BMI between 35 to 40 = Severely Obese
    BMI of 40 and over = Very Severely Obese

    """)
menu_message()
selection()