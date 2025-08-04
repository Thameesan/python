time=int(input("give your talked time-"))
total=0
'''
if 0<time<30:
	print(f"cash for last call is {time*2}rs")
elif :
	if 31<time<60:
		print(f"cash for last call is {30*2+(time-30)*1.5}rs")
	else:
		if 61<time<120:
			print(f"cash for last call is {30*2+30*1.5+(time-60)*1}rs")

		else:
			print(f"cash for last call is {30*2+30*1.5+60*1+(time-120)*0.5}rs")
'''

if 0<=time:
    if 120<time:
        total=(30*2+30*1.5+60*1+(time-120)*0.5)
    elif 61<time<120:
        total=30*2+30*1.5+(time-60)*1
    elif 31<time<60:
        total=30*2+(time-30)*1.5
    elif 0<time<30:
        total=time*2
    print(f"cash for talked time is {total}rs")
        
else: 
    print("invalide input")

