'''
first name
last name
2005 |342|         01550
       b or girl  
date of birth
age
'''
l_m_dates=[31,29,31,30,31,30,31,31,30,31,30,31]
#n_m_dates='31 29 31 30 31 30 31 31 30 31 30 31'
#l_m_dates.split()
#n_m_dates.split()
gender='in input' 
b_month=0
'''
f_name=input('enter your first name ')
while not(f_name.isalpha):
    f_name=input('enter your first name with out any number or blank')
l_name=input('enter your last name ')
while not(l_name.isalpha):
    l_name=input('enter your last name with out any number or blank') '''
ic_num=input('enter your ic number ')
while not(ic_num.isdigit) or len(ic_num)!=12:
    ic_num=input('incorrect input enter your ic number ') 
#b_date=input('enter your birthday date ') 
date=int(ic_num[4:7]) 
if date>=500:
    gender='female'
    date-=500
else:
    gender='male' 
for i in l_m_dates:
    if date>=0:
        date=date-i
        b_month=b_month+1
date+=l_m_dates[(b_month-1)]    
print(f'{b_month},{gender},{date}')
    


    
    


