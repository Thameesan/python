fav={}
for i in range (5):
    sub=input("enter your fav subject")
    
    for sub in fav.keys():
        if sub==i:
            fav[i]+=1
            break   
print(fav)