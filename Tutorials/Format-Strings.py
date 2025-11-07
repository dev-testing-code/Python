# String formatting lets you insert values into a string.

# 1. f-Strings (Formatted String Literals) - The modern and preferred way
name = "Alice"
age = 30

# Basic usage
print(f"My name is {name} and I am {age} years old.")

# You can also evaluate expressions inside
print(f"In 5 years, I will be {age + 5} years old.")

# Formatting numbers
price = 59.99
tax = 0.075
print(f"The price is ${price:.2f}") # Format to 2 decimal places
print(f"The tax is {tax:.1%}")   # Format as a percentage

# 2. The str.format() method
# Positional arguments
print("My name is {} and I am {} years old.".format(name, age))

# Keyword arguments
print("My name is {n} and I am {a} years old.".format(n=name, a=age))

# Mixed arguments
print("Hello, {}. Your balance is {:,.2f}.".format("John", 12345.67))

# Formatting with alignment and padding
# <: left-align
# >: right-align
# ^: center-align
text = "Python"
print("'{:<10}'".format(text)) # Left align in 10 spaces
print("'{:>10}'".format(text)) # Right align in 10 spaces
print("'{:^10}'".format(text)) # Center align in 10 spaces
print("'{:*^10}'".format(text))# Center align with * as padding

# 3. Percent (%) Formatting (The old way)
# You might see this in older Python code.
print("My name is %s and I am %d years old." % (name, age))

# For floating point numbers
print("The price is %.2f" % price)
