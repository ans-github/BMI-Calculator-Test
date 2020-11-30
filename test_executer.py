#Imported Modules & Libraries

from Functions.general_functions import menu_message, input_func
from Functions.selection import selection, selection_unit
from Functions.bmi_system import bmi_calc_imperial, bmi_calc_metric
import os
import sys
import datetime

#My BMI Calculator 07/09/2021 - Goal 80kg
#This is still in progress and many tweaks are still needed. However it does perform the function.

#Functions required:
# -Unit Converter e.g. KG,Stone,Lbs, CM, FT, Inches, Metres
# Date Settings
# File Save System 
# GUI Needs setting up
# Return to menu system


#date section
# now = datetime.now()
# print("now.month, now.year, now.day, now.second, now.hour, now.minute")


menu_message()
selection()
