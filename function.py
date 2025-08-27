'''
def printMyName(name):   #printMyName(argument)
    print(f'my name is {name}')  #print(f'my name is {perameter}')
''' 
'''  
printMyName('thameesan')
printMyName('kunalan')

'''
'''
def getFullName(firstName,lastName):
    print(firstName+lastName)
getFullName('selvanayagam','thameesan')

'''
'''
def getFullName(firstName="selvanayagam",lastName='thameesan'):
    print(firstName+lastName)
getFullName()
'''


def getFullName(firstName,lastName):
    print(firstName+lastName)
    #return firstName+lastName
#getFullName('hi ')
fullName=getFullName("selvanayagam",'thameesan')
print(fullName)