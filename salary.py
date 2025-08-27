'''
list=employ income
tax 50,000   3
	50,000 to 100,000 5
    100,000 to 300,000 8
	1000,000 to 10
'''

salary=[10000,20000,78907,234523,234567,335663,112335,12345,678944,562485,12554,88654]
month=[1,2,3,4,5,6,7,8,9,10,11,12]
monthName=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
tax=[0,0,0,0,0,0,0,0,0,0,0,0]
net_salary=[0,0,0,0,0,0,0,0,0,0,0,0]
total_salary=0
total_tax=0
print(f'{'month':<10}      \t{'salary':<10}\t{'tax':<10}\t{'net salary':<10}')
for i in month:
    if salary[i-1]<=50000:
        tax[i-1]=int(salary[i-1]*0.03)
    elif salary[i-1]>50000 and salary[i-1]<=100000:
        tax[i-1]=int(salary[i-1]*0.08)
    elif salary[i-1]>100000:
        tax[i-1]=int(salary[i-1]*0.10)
    net_salary[i-1]=salary[i-1]-tax[i-1]
    print(f'{monthName[i-1]:<10}\t{salary[i-1]:>12}\t{tax[i-1]:>12}\t{net_salary[i-1]:>12}')
    total_salary=total_salary+net_salary[i-1]
    total_tax=total_tax+tax[]
print(f'Total salary is {total_salary}')



        
