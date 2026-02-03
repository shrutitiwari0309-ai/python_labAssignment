# Read voltage and resistance from user
V = float(input("Enter Voltage (V): "))
R = float(input("Enter Resistance (Ohms): "))

# Calculate current using Ohm's Law
I = V / R

# Display current
print(f"Current (I) = {I:.2f} A")

# Determine nature of current
if I < 0.5:
    print("Low current")
elif 0.5 <= I <= 2:
    print("Normal current")
else:
    print("High current")
