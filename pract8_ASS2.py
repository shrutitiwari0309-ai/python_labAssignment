source = input("Enter source file name: ")
destination = input("Enter destination file name: ")

src = open(source, "r")
dest = open(destination, "w")

print("\nContent of Source File:\n")

for line in src:
    print(line, end="")
    stripped = line.strip()
    if not stripped.startswith("#") and stripped != "":
        dest.write(line)

src.close()
dest.close()

print("\n\nContent of Destination File (Without Comments):\n")

dest = open(destination, "r")
print(dest.read())
dest.close()