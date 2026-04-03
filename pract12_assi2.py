import pandas as pd

# Read Excel file
df = pd.read_excel("employee.xlsx")

# a) Employees in Automotive domain
print("Employees in Automotive domain:")
print(df[df['Department'] == 'Automotive'])
print()

# b) Details using Employee ID
emp_id = int(input("Enter Employee ID: "))
print("Employee Details:")
print(df[df['Employee ID'] == emp_id])
print()

# c) All Developers in Infosys
print("List of Developers:")
print(df[df['Designation'] == 'Developer'])