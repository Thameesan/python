x=[[10,20,30],
   [70,90,25],
   [40,90,26]
  ]
print(x[2][2])

for i in x:
    for y in i: 
        print(y)
        
i=0
while i<3:
    j=0
    while j<3:
        print(x[i][j])
        j+=1
    i+=1