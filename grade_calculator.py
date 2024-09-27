lab = int(input("Enter the number of labs completed: "))
quiz = int(input("Enter the number of quizzes completed: "))
ass1 = float(input("Enter grade for Assignment 1: "))
ass2 = float(input("Enter grade for Assignment 2: "))
ass3 = float(input("Enter grade for Assignment 3: "))
ass4 = float(input("Enter grade for Assignment 4: "))
mid1 = float(input("Enter grade for Midterm 1: "))
mid2 = float(input("Enter grade for Midterm 2: "))
final = float(input("Enter grade for Final Exam: "))
prep = float(input("Enter grade for Midterms and Final Preparation: "))
def labs(labs_done: int) -> float:
    if labs_done >6:
        return 1
    else:
        return (lab/6)
def quizzes(quizzes_done: int) -> float:
    if quizzes_done > 6:
        return 1
    else:
        return (quiz/6)
mark = (labs(lab)*20) + (quizzes(quiz)*15) + ((((ass1)+(ass2)+(ass3)+(ass4))/4)*0.16) + ((((mid1)+(mid2))/2)*0.25) + ((final)*0.18) + ((prep)*0.06)
print("Your grade is: ", round(mark,2))
