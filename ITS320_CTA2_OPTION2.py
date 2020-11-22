#------------------------------------------------------------------------
# Program Name:Vehicle Data 
# Author:Sarah Figueroa
# Date:10/19/19
#------------------------------------------------------------------------
# Pseudocode: This program will allow the User to type the Brand, Make, Model, Odometer Readings, and Gas Mileage and the
# program will then print out the car information in summary.
# Definition of get_number- these values are to be entered at numbers rather than letter values, if the user imputs a 
# letter they will then get a message to input a number. 
# Auto_details = The program will output a statement for the user to respond to and then prompot them enter a value. 
# The format is designed for the system to prompt the user to enter data based on the value in the following format- Data Item - Input- Output 
# The Auto Details dictionary is enclosed in brackets encompasing all the information for the program to give to the user to
#respond to. 
#Print(Auto Details)- will prompt the program to print the input and outputs of the program in a summary format 
#-----------------------------------------------------------------------
# Program Inputs: Brand, Model, Year, Starting Odometer number, Ending Odometer number, Gas Mileage number
# Program Outputs: 'Miles per gallon': Gas Mileage number, 'Car Model': Model, 'Ending odometer': Ending odometer number, 
# Starting Odometer': Starting Odometer number, 'Car Brand': Brand , 'Model Year': Year 
#------------------------------------------------------------------------

def get_number(hint):
    while True:
        try:
            value = int(input(hint))
        except ValueError:
            print('Please input a number')
            continue

        else:
            break
    return value
#Using this get_number definition will define how these values should be entered by the user. Without this definition the
#user would be able to type letters instead of numbers for the year, odometer readings and gas mileage. 

Auto_details =     {'Car brand': input('Car brand:'),
                   'Car model': input('Car model:'),
                   'Model Year': get_number('Model Year:'),
                   'Starting odometer reading': get_number('Starting odometer reading:'),     
                   'Ending odometer reading': get_number('Ending odometer reading:'),
                   'Miles per gallon': get_number('Miles per gallon:')}
print(Auto_details)