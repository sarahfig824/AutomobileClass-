#------------------------------------------------------------------------
# Program Name: Option #2:Cartesian Product AXB of two lits
# Author:Sarah Figueroa
# Date:11/23/19
#------------------------------------------------------------------------
# Pseudocode: The program compute the cartesian product of list A and B. 
# First need to define cartesian_product (A,B) by declaring an epty list product =[] and using two loops to return the cartesian product. 
# Print directions for user to enter first list for A followed by print directions for user to enter first list for B
# Print("AxB = ",cartesian_product(A,B)) uses the deined cartesian prouct and the given lists to print the products of the two lists as an output. 
# Program Inputs: List A numbers and List B numbers 
# Program Outputs: all the possible combinations of AXB 
#------------------------------------------------------------------------
# function that computes the cartesian product, AxB of two lists.
def cartesian_product(A,B):
    # declare empty list
    product = []
    # we use 2 loops
    for i in A:
        for k in B:
            # add product to list
            product.append((i,k))
    # return cartesian product
    return product
#Added Print after feedback from Professor to allow the user to enter their own numbers instead of having defaulted numbers in the code
print("This program creates the cartesian product of two lists")
print("Please, enter first list numbers up to ten numbers, separated with space in one line")
# read line and split by space
A = input(" ").split()
# convert strings to numbers
for i in range(len(A)):
    A[i] = int(A[i])
print("Please, enter second list numbers up to ten numbers, separated with space in one line")
# read line and split by space
B = input(" ").split()
# convert strings to numbers
for i in range(len(B)):
    B[i] = int(B[i])
# generate cartesian product and display it
print("AxB = ",cartesian_product(A,B))

input("Press Enter to continue...")




