class Employee:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.salary = 0
        self.address = ""

    # Method to take input
    def get_input(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.salary = float(input("Enter salary: "))
        self.address = input("Enter address: ")

    # Method to display details
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)


# Derived class
class Manager(Employee):
    def __init__(self):
        super().__init__()   # Call parent constructor
        self.department = ""

    def get_input(self):
        super().get_input()
        self.department = input("Enter department: ")

    def display(self):
        super().display()
        print("Department:", self.department)
        print("-------------------------")


# Main program
managers = []

for i in range((10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      )):
    print(f"\nEnter details for Manager {i+1}")
    m = Manager()
    m.get_input()
    managers.append(m)

print("\n--- Manager Details ---")
for m in managers:
    m.display()