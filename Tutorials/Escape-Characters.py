# Escape characters are used to insert characters that are illegal in a string.
# An escape character is a backslash \ followed by the character you want to insert.

# 1. To insert quotes inside a string

# You can use double quotes inside single quotes, and vice-versa
print('It\'s alright.')
print("He is called \"Johnny\"")

# Or you can use an escape character
print('It\'s alright.')
print("He is called \"Johnny\"")

# 2. Common Escape Characters

# \\ - Backslash
print("This will insert one \\ (backslash).")

# \n - New Line
print("Hello\nWorld!")

# \r - Carriage Return
# A carriage return moves the cursor to the beginning of the line
print("Hello\rWorld!") # Notice how "World!" overwrites "Hello"

# \t - Tab
print("Hello\tWorld!")

# \b - Backspace
# This example erases one character (the space)
print("Hello \bWorld!")

# \f - Form Feed (rarely used in modern terminals)
print("Hello\fWorld!")

# Octal and Hex values
# You can use octal or hex values to represent characters
print("\110\145\154\154\157") # Octal for "Hello"
print("\x48\x65\x6c\x6c\x6f") # Hex for "Hello"

# 3. Raw Strings
# If you don\'t want characters prefaced by \ to be interpreted as escape sequences,
# you can use raw strings by adding an r before the first quote.

# Without a raw string, this would be an error or unintended behavior
# print("C:\Users\Test") # \U starts a Unicode escape

# With a raw string, the backslashes are treated as literal characters
print(r"C:\Users\Test")
