'''
list1=['maths','tamil','english','ict']
print(list1)
print(f'list1[1]{list1[1]}')
print(f'list1[-5]{list1[-3]}')
print(len(list1))
'''
'''
list1=['maths','tamil','english','ict']
len_of_list1=len(list1)
while len_of_list1>0:
    len_of_list1-=1
    print(list1[len_of_list1])
print(type(list1))
'''
'''
list1=['maths','tamil','english','ict']
print(list1)
list1[0]='history'
print(list1)
'''
list1=['maths','tamil','english','science','ict']
x=0
'''
while x<len(list1):
    #a=input('enter subject ')
    list1[x]=input('enter subject ')
    x+=1
print(list1)
'''
'''
for i in range(0,len(list1)):
    list1[i]=input(f'enter subject replase with {list1[i]} ')
print(list1)    
'''
'''
x=0
for i in list1:
    list1[x]=input(f'enter subject replase with {i} ')
    x+=1
print(list1)    
'''
print(list1[1:5])   
print(list1[:5]) 
print(list1[2:])     
print(list1[::2]) #step 2 
print(list1[::3]) #step3

