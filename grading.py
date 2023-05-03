#script to print student name and each subject score
def student_score():
 name = (input('Enter your name :\n')) 
 marks = int(input('Enter your score 1 : '))
 biology_grade = 68 
 grade = ""
 maths_grade = 70
 if marks > 75 :
  grade = 'A'
 elif marks >= 70 and marks < 75:
  grade = 'A-'
 elif marks >= 69 and marks < 70:
  grade = 'B+'
 elif marks >= 62 and marks < 69:
  grade = 'B'
 elif marks >= 55 and marks < 62:
  grade = 'B-'
 elif marks >= 46 and marks < 55:
  grade = 'C+'


 print('Student name:' + name )
 print('Subjects:' + 'Biology:' , biology_grade)
 print('Subject:' +  grade )
 print('subject:' + maths_grade)

student_score()