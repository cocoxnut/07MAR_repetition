app = input("Applications you know: ")
age = int(input("Enter your age: "))
expert = int(input("Enter experience in years: "))
salary = int(input("Enter your preferred salary: "))
if app == 'java' and 'python' or 'javascript' and age >= 18 and age <= 65 and expert > 3 and salary <= 60000:
    print("Accepted")
else:
    print("Not acceptable") 
