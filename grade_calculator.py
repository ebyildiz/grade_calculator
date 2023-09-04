"""This grade calculator can take categories with 
their percentages as a dictionary and calculate your final grade!""" 

grade_indicators = {}  # Create an empty dictionary to store the data
user_grades = []
while True:
    key = input("Enter a grade indicator such as 'Assignments' \
(or press Enter to stop): ")
    if not key:
        break  # If the user presses Enter without entering a key, exit the loop
    value = float(input("Enter its percentage: "))
    user_grade = float(input("Enter your grade out of 100: "))
    user_grades.append(user_grade)
    grade_indicators[key] = value  # Add the key-value pair to the dictionary

indicators=list(grade_indicators.keys()) #Seperate indicators in a list to use later

def grade_calc(percentages, grades): 
    """A grade calculator that takes the percentages as a dictionary and user's
grades as a list. Then it prints the final grade of that person for the class"""
    seperate_grades = []
    for i in range(len(percentages.keys())):
        seperate_grades.append(percentages[indicators[i]] * grades[i])
    print("Your final grade is: " + f"{round(sum(seperate_grades)/100, 2)}")

grade_calc(grade_indicators, user_grades) #result! :)