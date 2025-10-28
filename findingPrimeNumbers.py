primeNumbers=[]
for i in range(1,101):
    mod=0
    if i==1:
        print(i)
        primeNumbers.append(i)
    if i>1:
        for x in range(2,i):
            mod=i%x
            if mod==0:
                break
        if mod!=0:
            print(i)
            primeNumbers.append(i)
print(f'These are the prime numbers between {1} to {100}')
print(primeNumbers)           
            
    
    
    
    
    
    
    
    
    