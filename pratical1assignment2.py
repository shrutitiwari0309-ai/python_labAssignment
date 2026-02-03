class Vendor:
    def __init__(self, name, year, contact, email):
        self.name = name
        self.year = year
        self.contact = contact
        self.email = email
        self.monthly_purchases = []

    def read_monthly_purchases(self):
        print("\nEnter purchase amount for each month:")
        for i in range(1, 13):
            amount = float(input(f"Month {i}: "))
            self.monthly_purchases.append(amount)

    def generate_annual_report(self):
        total = sum(self.monthly_purchases)

        print("\n----- ANNUAL PURCHASE / BILLING REPORT -----")
        print(f"Vendor Name       : {self.name}")
        print(f"Year of Association: {self.year}")
        print(f"Contact Number    : {self.contact}")
        print(f"Email ID          : {self.email}")
        print("\nMonthly Purchases:")
        
        for i, amount in enumerate(self.monthly_purchases, start=1):
            print(f"Month {i}: {amount:.2f}")

        print("-------------------------------------------")
        print(f"Total Annual Purchase: {total:.2f}")
        print("-------------------------------------------")


# Main Program
name = input("Enter Vendor Name: ")
year = int(input("Enter Year of Association: "))
contact = input("Enter Contact Number: ")
email = input("Enter Email ID: ")

vendor = Vendor(name, year, contact, email)
vendor.read_monthly_purchases()
vendor.generate_annual_report()
