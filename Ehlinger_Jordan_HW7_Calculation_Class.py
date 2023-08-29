#Author: Jordan Ehlinger
#Assignment Number & Name: HW7 Return on Investment - Calculation Class
#Due Date: N/A
#Program Description: Holds calculation class to receive initial and current value and calculate ROI and return it as a variable.


#create calculation class
class CalculationClass:

    #init function to initialize variables
    def __init__(self):
        self.__initial=0
        self.__current=0
        self.__ROI=0

    #set functions for initial and current
    def set_initial(self,initial):
        self.__initial=initial
    
    def set_current(self,current):
        self.__current=current

    #get functions for initial and current
    def get_initial(self):
        return self.__initial

    def get_current(self):
        return self.__current

    #get function for ROI
    def get_ROI(self):
        return self.__ROI

    #function for calculating ROI
    def calculate_ROI(self):
        try:
            self.__ROI = (self.__current - self.__initial) / self.__initial
        except:
            print("Cannot calculate ROI since initial value is 0")

    #string function to display output
    def __str__(self):
        return "The ROI for this investment is " + format(self.__ROI, '.2%')
