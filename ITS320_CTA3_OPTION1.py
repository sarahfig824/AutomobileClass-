#------------------------------------------------------------------------
# Program Name:Ferrari Value 
# Author:Sarah Figueroa
# Date:10/26/19
#------------------------------------------------------------------------
# Pseudocode:This program will prompt the user to type the year of the Ferrari 250 GTO and the sytem will tell the user the value of the car for that year. 
# Definition of get_number- these values are to be entered at numbers rather than letter values, if the user imputs a 
# letter they will then get a message to input a year. 
# year= get_number ('Enter year:')- Enter year is the prompt on the screen for the user to enter the year of the Ferrari
# If year= because no models were made before 1962 and after 2014 the IF phrase is used to prompt the system to give a textual message 
# elif year= will look through the different year blocks until it finds a TRUE value and will then spit out the value for that year block 
# print ( $, value)- will print the value of the car for that year in the format of a $ then numeric value
#-----------------------------------------------------------------------
# Program Inputs: Year
# Program Outputs: Car Value 
#------------------------------------------------------------------------


def get_number(hint):
    while True:
        try:
            value = int(input(hint))
        except ValueError:
            print('Please input a year')
            continue

        else:
            break
    return value
#Using this get_number definition will define how these values should be entered by the user. Without this definition the
#user would be able to type letters instead of numbers for the year. 

year = get_number('Enter year:')

if year <= 1961:
   print('Ferrari 250 GTO was not made during this year')

elif year <= 1964:
   print('$', 18500)

elif (year >= 1965) and (year <= 1968):
   print('$', 6000)   

elif (year >= 1969) and (year <=1971):
   print ('$', 12000)

elif (year >= 1972) and (year <= 1975):
   print ('$', 48000)

elif (year >= 1976) and (year <= 1980):
   print ('$', 200000)

elif (year >= 1981) and (year <= 1985):
   print ('$', 650000)

elif (year >= 1986) and (year <= 2012):
   print ('$', 35000000)

elif (year >= 2013) and (year <= 2014):

   print ('$', 52000000)

if year >= 2015:
   print ('No value available for Ferrari 250 GTO for that year')
2