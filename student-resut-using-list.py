pass_grade = ['A','B','C','D']
failed = 'F'
grade = input("Please Enter Your Grade ")

if grade.upper() in pass_grade or grade.lower() in pass_grade:
    print('Congratulation')
elif grade.upper() == failed or failed.lower() == failed:
    print('Good Luck Next Year')
else:
    print('Please Enter Correct Grade')
