time=int(input("give your talked time"))
if 0<time<30:
	print(f"cash for last call is {time*2}rs")
else:
	if 31<time<60:
        print(f"cash for last call is {30*2+(time-30)*1.5}rs)
	else:
		if 61<time<120:
		print(f"cash for last call is {30*2+30*1.5+(time-60)*1}rs