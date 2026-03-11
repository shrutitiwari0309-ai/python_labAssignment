# Enter prices of sold items separated by space
prices = tuple(map(int, input("Enter prices of sold items: ").split()))

# a) Total number of items sold
print("Total items sold:", len(prices))

# b) Price of the cheapest item
print("Cheapest item price:", min(prices))

# c) Price of the costliest item
print("Costliest item price:", max(prices))

# d) Price list in ascending order
print("Prices in ascending order:", tuple(sorted(prices)))

# e) Number of costliest items sold
costliest = max(prices)
print("Number of costliest items sold:", prices.count(costliest))