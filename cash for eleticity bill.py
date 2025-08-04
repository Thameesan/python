unit=int(input('enter used unit- '))
total=0
tax=0

if 0<=unit:
    if 0<=unit<=90:
        total=unit*7
    elif 91<=unit<=150:
        total=90*7+(unit-90)*10
    elif 151<=unit:
        total=90*7+60*10+(unit-150)*15
        if 300<unit:
            tax=total*3/100
            
    print(F"your bill is- {total+tax}rs")
        
        
    
    
    
else:
    print("invalid unit")