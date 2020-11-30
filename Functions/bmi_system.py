from Functions.general_functions import menu_message, input_func

#Calculations (metric and imperial)
def bmi_calc_metric():
    my_input = int(input("please enter your weight in KG: "))
    my_input2 = int(input("please enter your height in cm: "))
    bmi_result_met = my_input / my_input2 / my_input2 * 10000
    print("Your BMI is " + str(bmi_result_met))
    input("Please press any key to exit program...")

def bmi_calc_imperial():
    my_input = int(input("Please enter your weight in lbs: "))
    my_input2 = int(input("Please enter your height in inches: "))
    bmi_weight = my_input * 703
    bmi_height = my_input2 * my_input2
    bmi_result_imp = bmi_height / bmi_weight
    print("Your BMI is " + str(bmi_result_imp))
    input("Please press any key to exit program...")