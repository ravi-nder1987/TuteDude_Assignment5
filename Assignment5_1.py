#Program to searching marks of input student from the dictonary

student_marks={'Ravi':90,'Rahul':85,'Alice':85,'Sachin':99}
student_name=input('Enter the student\'s name:')
if (student_name in student_marks):
    print(student_name +'\'s'+ ' marks:',student_marks[student_name])
else:
    print('Student not found')