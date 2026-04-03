import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("company_sales_data.csv")

# Display first 5 rows
print(data.head())

# a) Total profit of all months using Line Plot
plt.figure(figsize=(8,5))
plt.plot(data['month_number'], data['total_profit'], marker='o')
plt.title("Total Profit per Month")
plt.xlabel("Month Number")
plt.ylabel("Total Profit")
plt.grid(True)
plt.show()

# b) All product sales using Multiline Plot
plt.figure(figsize=(10,6))
plt.plot(data['month_number'], data['facecream'], label='Face Cream')
plt.plot(data['month_number'], data['facewash'], label='Face Wash')
plt.plot(data['month_number'], data['toothpaste'], label='Toothpaste')
plt.plot(data['month_number'], data['bathingsoap'], label='Bathing Soap')
plt.plot(data['month_number'], data['shampoo'], label='Shampoo')
plt.plot(data['month_number'], data['moisturizer'], label='Moisturizer')

plt.title("Sales Data of All Products")
plt.xlabel("Month Number")
plt.ylabel("Sales Units")
plt.legend()
plt.grid(True)
plt.show()

# c) Face cream and face wash sales using Bar Chart
plt.figure(figsize=(8,5))
plt.bar(data['month_number'] - 0.2, data['facecream'], width=0.4, label='Face Cream')
plt.bar(data['month_number'] + 0.2, data['facewash'], width=0.4, label='Face Wash')

plt.title("Face Cream and Face Wash Sales")
plt.xlabel("Month Number")
plt.ylabel("Sales Units")
plt.legend()
plt.show()

# d) Total sale data for last year using Pie Chart
sales_data = [
    data['facecream'].sum(),
    data['facewash'].sum(),
    data['toothpaste'].sum(),
    data['bathingsoap'].sum(),
    data['shampoo'].sum(),
    data['moisturizer'].sum()
]

labels = ['Face Cream', 'Face Wash', 'Toothpaste', 'Bathing Soap', 'Shampoo', 'Moisturizer']

plt.figure(figsize=(7,7))
plt.pie(sales_data, labels=labels, autopct='%1.1f%%')
plt.title("Yearly Sales Distribution")
plt.show()
