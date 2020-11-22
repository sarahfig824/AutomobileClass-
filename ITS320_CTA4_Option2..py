#------------------------------------------------------------------------
# Program Name:Repetition Control Structure – Grade Statistics
# Author:Sarah Figueroa
# Date:11/3/2019
#------------------------------------------------------------------------
# Pseudocode:This program will prompt the user to type 5 test scores and will then tell the user the min score, max score and average score. 
# Definition of get_number- these values are to be entered at numbers rather than letter values, if the user imputs a 
# letter they will then get a message to input a numeric score. 
# get_scores() is the 5 different test scores that the user will input. Total will add the sum of all 5 scores in order to calcuate the average. 
# def_get scores() Test_scores defines what the scores are. "For scores in range (5)" define the loop of the code. The 5 indicates 5 times that the user will enter a score. 
# value = float(input('Enter score: ') converts the input of scores into a float and will return the test scores printed as an average, minimum and maximum.
#-----------------------------------------------------------------------
# Program Inputs: five test scores 
# Program Outputs: minimum, maximum, average
#------------------------------------------------------------------------

def get_number(hint):
    while True:
        try:
            value = int(input(hint))
        except ValueError:
            print('Please input a numeric score')
            continue

        else:
            break
    return value
    
def main():
    scores = get_scores()
    total = sum(scores)
    average = total/len(scores)
    print('The lowest test score is: ', min(scores))
    print('The highest test score is: ', max(scores))
    print('The average test score is: ', average)

def get_scores():
    test_scores = []
    for scores in range(5):
        value = float(get_number('Enter score: '))
        test_scores.append(value)
    return test_scores
main()