#Python Dictonaries can be iterated over list

emp = {"james" : 9998887775,"john" : 7778886665}
for name,number in emp.items():
	print("Employee Contact Number %s is %d" %(name, number))
