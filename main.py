#Variable
company = "Lebanese Spotlight" #string
founded = 2017 #interger
tax_rate= 0.11 #float
is_active = True # Boolean

print("="*35)
print(f"Company Name is:{company}")
print(f"Company Founded in :{founded}")
print(f"Active: {is_active}")
print("="*35)


#Dictionary
employee = {  #key:value
    "name" : "Rabih",
    "department":"IT",
    "salary" : 500
}

print("Single Employee Information")
print(employee)
print("Name:",employee["name"])
print("Salary:", employee["salary"])
print()


#List of Dictionary

employees = [
    {"name": "Rabih", "department": "IT", "salary": 2000}, # index 0
    {"name": "Sarah", "department": "HR", "salary": 1800}, # index 1
    {"name": "John", "department": "Finance", "salary": 2500}, # index 2
    {"name": "Lana", "department": "Finance", "salary": 2500} # index 3
]

print(employees[0]["department"])
print(employees[1]["name"])
print(f"Name is {employees[1]["name"]}")

#Loop
print("Employee List")
print("-"*35)

for each_employee in employees :
    print(f"Name is {each_employee["name"]}")
    print()
print("bcb")


#Condition

salary = int(input("Enter you salary: "))
print(f"Your Salary is: {salary}")

if salary >=2000:
   print ("You are gaining a good salary")
else:
    print("You need to find another JOB NOWWWW!!!!!!!")


print("Hello Github")
