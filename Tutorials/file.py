# Open the file in read mode
file = open("example.txt", "w+")

# Read the entire content of the file
content = file.read()
print(content)

# Write some content to the file
file.write("Hello, World!\n")
file.write("Writing to a file in Python is simple.\n")

# Close the file
file.close()