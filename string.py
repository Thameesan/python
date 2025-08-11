s='Welcome to python'
'''
'welcome to python'
'123.............17'
'-17.............-1'


'''
'''
print(s)
print(len(s))
print(s[0])
print(s[-17])
i=1
while i<len(s):
    print(s[i])
    i+=1
    
''' 
'''   
for i in s:
    print(i)
''' 

'''
i=len(s)-1
while i>=0:
    print(s[i])
    i-=1
'''
'''
i=-abs(len(s)) # len(s)*(-1) # -len(s)
while i<=-1:
    print(s[i])
    i+=1
'''
'''
for i in range (len(s)-1,-1,-1):
    print(s[i])


'''
'''
for i  in reversed(s):
    print(i)
'''

#print(reversed(s)) it is not working


a=s[0:5]
print(a)

b=s[8:10]
print(b)

c=s[-17:-12]
print(c)









  