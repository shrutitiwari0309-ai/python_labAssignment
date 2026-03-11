# Ask the user to enter integers separated by space
nums = input("Enter a series of integers: ")

# Convert input into a tuple
t = tuple(map(int, nums.split()))

# a) Print total number of items
print("Total number of items:", len(t))

# b) Print last item
print("Last item in the tuple:", t[-1])

# c) Print tuple elements in reverse order
print("Tuple in reverse order:", t[::-1])

# d) Check if tuple contains integer 5
if 5 in t:
    print("Yes")
else:
    print("No")

# e) Remove first and last items, sort remaining items
new_t = t[1:-1]
sorted_t = tuple(sorted(new_t))
print("Sorted tuple after removing first and last items:", sorted_t)