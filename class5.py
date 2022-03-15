s = int(input("Enter your salary: "))
w = int(input("Enter number of calendar days: "))
d = int(input("Number of work days: "))
b = int(input("Amount of bonus: "))
f = int(input("Amount of fines payable: "))
n = 13
salary = ((s / w * d + b) * ((100 - n) / 100) - f)
print(salary) 
