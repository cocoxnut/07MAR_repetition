name = input("Enter name of file: ")
if name.count(".") >= 1 :
	x = name.split(".")
	print("Your extension is","-", x[1])
else : 
	print("Your extension is not found")    
