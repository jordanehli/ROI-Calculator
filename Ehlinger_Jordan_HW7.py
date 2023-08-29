#Author: Jordan Ehlinger
#Assignment Number & Name: HW7 Return on Investment
#Due Date: N/A
#Program Description: Holds the main function which calls input functions and the calculate ROI function and then displays the results.


#import classes from other files
import Ehlinger_Jordan_HW7_Validation_Class
import Ehlinger_Jordan_HW7_Calculation_Class

def main():
    #create variable for validation function call
    validation = Ehlinger_Jordan_HW7_Validation_Class.ValidationClass()

    #intentional bad value to initialize
    initial_value = -1
    #while loop to get initial value and run it through validation function
    while initial_value == -1:
        initial_value_input = input("What is the initial value? ")
        initial_value = validation.checkFloat(initial_value_input)
        if initial_value == -1:
            print("The initial value must be a positive number.")
        
    #intentional bad value to initialize
    current_value = -1
    #while loop to get initial value and run it through validation function
    while current_value == -1:
        current_value_input = input("What is the current value? ")
        current_value = validation.checkFloat(current_value_input)
        if current_value == -1:
            print("The current value must be a positive number.")


    #create variable for calculation function call
    calculation = Ehlinger_Jordan_HW7_Calculation_Class.CalculationClass()

    #send inputs to calculation functions
    calculation.set_initial(initial_value)
    calculation.set_current(current_value)

    #call ROI calculation function
    calculation.calculate_ROI()

    #call string function to display the ROI calculation result
    print(calculation)
    

#call main
main()
