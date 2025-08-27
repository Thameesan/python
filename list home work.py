student=[]
subject=[]
marks=[]
result=[]
average=[]
number_of_students=int(input("enter number of students-"))
number_of_subjects=int(input('number of subjects-'))
for i in range (number_of_students):
    student.append(input(f'enter student {i+1}name-'))
for i in range (number_of_subjects):
    subject.append(input(f'enter subject {i+1} name-'))
x=0
for x in range (number_of_subjects):
    m_list=[] 
    for i in range (number_of_students):
        m_list.append(input(f"enter {student[i]}'s {subject[x]} marks-"))
    marks.append(m_list)
    print()
    x+=1
print(marks)  
for i in range (number_of_students):
    total=0
    for y in range (number_of_subjects):
        total=total+int(marks[y][i])    
    average.append(total/number_of_subjects)
print(average)
'''    
print(f"Student Name  Physics   Maths    Chemistry  Total  Average  Result")
for i in student:
    if Average >= 75:
        result = "A"
    elif Average <75 and Average >= 65:
        result = "B"
    elif Average < 65:
        result = "C"
    
    print(f"{Stu_Name[i-1]:<12} {Marks_list[0][i-1]:>8} {Marks_list[1][i-1]:>8} {Marks_list[2][i-1]:>8} {Total:>8} {Average:>8} {result:>8}")
'''