import os
import sys
import datetime

#testing git changes. line 5

#My BMI Calculator 07/09/2021 - Goal 80kg
#This is still in progress and many tweaks are still needed. However it does perform the function.
#Functions required:
# -Unit Converter e.g. KG,Stone,Lbs, CM, FT, Inches, Metres
# Selection Menu
# Date Settings
# File Save System 

#Useful Variables
menu_message = """ Thank you for using this app, please select from options:
[1] Input Weight
[2] Print History
[3] Exit Application
"""
print(menu_message)

reg_input = int(input("Please enter your input: "))
my_input = int(input("please enter your weight in KG: "))
my_input2 = int(input("please enter your height in cm: "))
bmi = my_input / my_input2 / my_input2 * 10000
print(int(bmi))

#date section

# now = datetime.now()
# print("now.month, now.year, now.day, now.second, now.hour, now.minute")

#Calculation Selection
 

#Selection from menu


#exit program

def exit():
    sys.exit()