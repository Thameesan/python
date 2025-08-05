'''
    1 -1000 500/
    1000 3000  pre3/
    3000  10000 pre 5
    10000  per 10

    0777861677
'''


total=0
basic_prise=500
prise_for_1000_to_3000 =3 
prise_for_3000_to_10000=5
prise_for_over_10000=10

leter=int(input('enter leters used- '))

if 0<leter:
    if 1<leter and leter<=1000:
        total=basic_prise 
    elif 1000<leter and leter<=3000:
        total=basic_prise+(leter-1000)*prise_for_1000_to_3000
    elif 3000<leter and leter<=10000:
        total=basic_prise+2000*prise_for_1000_to_3000+(leter-3000)*prise_for_3000_to_10000
    elif 10000<leter:        
        total=basic_prise+2000*prise_for_1000_to_3000+7000*prise_for_3000_to_10000+(leter-10000)*prise_for_over_10000
    print(f'your leter={leter} your bill is {total}rs')    
else:
    print("invalid input")
    