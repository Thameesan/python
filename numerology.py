a_num=0  #a_num meaning addend_num

b_date=input('enter yor birthady date [yyyy/mm/dd]-')

while b_date[4]!="/" or b_date[7]!="/" or int(b_date[0])>2 or int(b_date[8:10])>31 or int(b_date[5:7])>12 :
    print(f'please follow the order when enter birthady')
    b_date=input('the order is yyyy/mm/dd - ')
b_num=str(b_date[8:10])
for i in b_date:
    if i!='/':
        a_num=a_num+int(i)
while len(str(a_num))>=2:
    a_num=str(a_num)
    a_num=int(a_num[0])+int(a_num[1])
while len(str(b_num))>=2:
    b_num=str(b_num)
    b_num=int(b_num[0])+int(b_num[1])
print(f'birthday number is {b_num}\n addend number is {a_num}')

