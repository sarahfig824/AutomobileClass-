#------------------------------------------------------------------------
# Program Name: Option #2: Third String in Reverse Order
# Author:Sarah Figueroa
# Date:11/10/19
#------------------------------------------------------------------------
# Pseudocode: The program will prompt the user to enter 3 string values and the system will return the concatenation of the first two strings and will print the 
# print the third string in reverse order. 
# def rev (one, two, three) tells the system how to arrange the numbers in reverse order and then how to print them. Return one + two tells the system the 
# def of the first two strings. def main () takes the users input of three different strings. Print concatenation of the first two string passes the three arguments using the calling 
# to print the concatenation rather than the reverse.
# Program Inputs: 3 string values 
# Program Outputs: concatenation of the first two strings, third string in reverse order 
#------------------------------------------------------------------------


def rev(one, two, three):
    print("Reverse of the third string is:",three[::-1])

    return one + two  # returns the concatenation (combination) of the first two strings

def main():

#User Inputs 3 different string values 
    first = input("Enter 1st string:")
    second = input("Enter 2nd string:")
    third = input("Enter 3rd string:")


    
    print("Concatenation of the first two strings is:",rev(first, second, third)) # calling function, passing three arguments

main()