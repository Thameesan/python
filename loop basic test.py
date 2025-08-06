x=1
while x<=10:
    if x%2==1:
        print(x,end=' ')
    x+=1  
print('') 
 
x=1
while x<=15:
    if x%2==0:
        print(x,end=' ')
    x+=1      
print('')  

x=1
y=1
total=1
while y<=5:
    while x!=y:  
        x+=1
        total=total+x
    print(total,end=" ")
    y+=1
print()


x=1
while x<=5:
    print(x*x,end=" ")
    x+=1
print('')

x=1
while x<=5:
    if x%2==1:
        print(x,end='')
    else:
        print('*',end='')
    x+=1
print('')

x=1
while x<=5:
    print(x,end='')
    if x%2==1:
        print('*')
    else:
        print('**')
    x+=1
print('')

x=1
y=1
while y<=5:
    x=1
    while x<=5:
        print(x,end='')
        x+=1
    print("")
    y+=1
print('')

x=1
y=1
while y<=5:
    x=5
    while x>=1:
        print(x,end='')
        x-=1
    print("")
    y+=1
print('')



x=1
y=1
while y<=5:
    x=1
    while x<=5:
        print(y,end='')
        x+=1
    print()
    y+=1
print('')

x=1
y=5
while y>0:
    x=1
    while x<=5:
        print(y,end='')
        x+=1
    print()
    y-=1
print()


x=1
y=1
while y<=5:
    for i in range(0,y):
        print('*',end='')
        x-=1
    print()
    y+=1
print('')


x=1
y=1
while y<=6:
    x=1
    while x!=y:
        print('*',end='')
        x+=1
    print()
    y+=1


x=1
y=1
while y<=6:
    x=1
    while x!=y:
        print(x,end='')
        x+=1
    print()
    y+=1






