
while True:

    numGrade = input("Please enter your numeric grade: ")
    if numGrade >= "90":
        print("You have a letter grade of A")
    elif numGrade >= "80" and numGrade <= "89":
        print("You have a letter grade of B")
    elif numGrade >= "70" and numGrade <= "79":
        print("You have a letter grade of C")
    elif numGrade >= "60" and numGrade <= "69":
        print("You have a letter grade of D")
    elif numGrade <= "59":
        print("You have a letter grade of F")

    user_input = input("Would you like to enter a new numeric grade? Y/N: ")
    if user_input == "Y" or user_input == "y":
        continue
    else:
        break

# Instead of typing elif numGrade >= "80" and numGrade <= "90" (and so on) I
# opted to only include 9 points in between to avoid confusion for when
# a grade is one of the "tens" (60, 70, 80, 90). If I hadn't done so, a "70"
# could be seen as both a C and a D.

# the while true function allows it to loop if the user wishes to do so. If the
# user opts out of it, the function then breaks.
