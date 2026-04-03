import pandas as pd

# 1. Create the Dataset
data = {
    'State': ['Rajasthan', 'Maharashtra', 'Madhya Pradesh', 'Uttar Pradesh', 'Gujarat'],
    'Area_km2': [342239, 307713, 308252, 240928, 196024],
    'Population': [81000000, 126000000, 85000000, 230000000, 70000000]
}
df = pd.DataFrame(data)

# a) Print the complete information of states
print("--- Complete State Information ---")
print(df)
print("\n")

# b) Print the name of the State having largest Area
largest_area = df.loc[df['Area_km2'].idxmax(), 'State']
print(f"State with largest Area: {largest_area}")

# c) Print the name of State having largest population
largest_pop = df.loc[df['Population'].idxmax(), 'State']
print(f"State with largest Population: {largest_pop}")
print("\n")

# d) Create a mechanism to calculate the population density of States
df['Density_per_km2'] = (df['Population'] / df['Area_km2']).round(2)
print("--- State Data with Population Density ---")
print(df)
print("\n")

# e) Determine the name of State with highest population density
highest_density = df.loc[df['Density_per_km2'].idxmax(), 'State']
print(f"State with highest Population Density: {highest_density}")