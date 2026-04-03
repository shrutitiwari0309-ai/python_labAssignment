import matplotlib.pyplot as plt
import pandas as pd

# Create dataset
companies = ['Microsoft', 'Google', 'Amazon', 'IBM', 'Deloitte', 
             'Capgemini', 'ATOS', 'Amdocs']
recruitments = [120, 150, 180, 100, 90, 110, 80, 95]

data = pd.DataFrame({
    'Company': companies,
    'Recruitments': recruitments
})

print(data)

# a) Bar Chart
plt.figure(figsize=(8,5))
plt.bar(data['Company'], data['Recruitments'])
plt.title("Company Recruitments - Bar Chart")
plt.xlabel("Company")
plt.ylabel("Number of Recruitments")
plt.xticks(rotation=45)
plt.show()

# b) Pie Chart
plt.figure(figsize=(7,7))
plt.pie(data['Recruitments'], labels=data['Company'], autopct='%1.1f%%')
plt.title("Recruitment Distribution")
plt.show()

# c) Customized Pie Chart
plt.figure(figsize=(7,7))
explode = [0.1, 0, 0, 0, 0, 0, 0, 0]

plt.pie(data['Recruitments'],
        labels=data['Company'],
        autopct='%1.1f%%',
        explode=explode,
        shadow=True)

plt.title("Customized Recruitment Pie Chart")
plt.show()

# d) Doughnut Chart
plt.figure(figsize=(7,7))
plt.pie(data['Recruitments'],
        labels=data['Company'],
        autopct='%1.1f%%',
        wedgeprops={'width':0.4})

plt.title("Doughnut Chart")
plt.show()

# Compare IBM and Amdocs
compare_companies = ['IBM', 'Amdocs']
compare_values = [100, 95]

plt.figure(figsize=(6,4))
plt.bar(compare_companies, compare_values)
plt.title("IBM vs Amdocs Recruitments")
plt.ylabel("Number of Recruitments")
plt.show()