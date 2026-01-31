name = input()
emp_id = int(input())
department = input()
basic_salary = float(input())

da = 0.92 * basic_salary
hra = 0.58 * basic_salary
ta = 0.30 * basic_salary

gross_salary = basic_salary + da + hra + ta
net_salary = gross_salary - 500

print(name)
print(emp_id)
print(department)
print(f"{net_salary:.2f}")
