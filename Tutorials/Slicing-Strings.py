# Slicing allows you to get a substring

# Basic slicing [start:stop]
# The 'stop' index is not included
s = "Hello, World!"
print(s[0:5])  # Output: Hello
print(s[7:12]) # Output: World

# Slicing from the beginning
# If you omit the start index, it defaults to 0
print(s[:5])   # Output: Hello

# Slicing to the end
# If you omit the stop index, it goes to the end of the string
print(s[7:])   # Output: World!

# Slicing with a step [start:stop:step]
# The step is the interval between characters to include
s = "0123456789"
print(s[0:10:2]) # Output: 02468
print(s[1:10:3]) # Output: 147

# Negative Indexing
# Negative indices count from the end of the string
s = "Python"
print(s[-1])   # Output: n
print(s[-3:])  # Output: hon
print(s[:-3])  # Output: Pyt

# Reversing a string with slicing
# A step of -1 reverses the string
s = "Hello"
print(s[::-1]) # Output: olleH
