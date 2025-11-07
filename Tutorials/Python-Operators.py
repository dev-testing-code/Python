# Operators are used to perform operations on variables and values.

# 1. Arithmetic Operators
print("--- Arithmetic Operators ---")
x = 10
y = 3
print(f"x + y = {x + y}")   # Addition
print(f"x - y = {x - y}")   # Subtraction
print(f"x * y = {x * y}")   # Multiplication
print(f"x / y = {x / y}")   # Division
print(f"x % y = {x % y}")   # Modulus (remainder)
print(f"x ** y = {x ** y}") # Exponentiation (x to the power of y)
print(f"x // y = {x // y}") # Floor division (rounds down to the nearest whole number)

# 2. Assignment Operators
print("\n--- Assignment Operators ---")
a = 5
print(f"a = 5 -> a is {a}")
a += 3 # same as a = a + 3
print(f"a += 3 -> a is {a}")
a -= 2 # same as a = a - 2
print(f"a -= 2 -> a is {a}")
# This pattern continues for *, /, %, //, **

# 3. Comparison Operators
print("\n--- Comparison Operators ---")
x = 5
y = 10
print(f"x == y: {x == y}") # Equal
print(f"x != y: {x != y}") # Not equal
print(f"x > y:  {x > y}")  # Greater than
print(f"x < y:  {x < y}")  # Less than
print(f"x >= y: {x >= y}") # Greater than or equal to
print(f"x <= y: {x <= y}") # Less than or equal to

# 4. Logical Operators
print("\n--- Logical Operators ---")
x = True
y = False
print(f"x and y: {x and y}") # Returns True if both statements are true
print(f"x or y:  {x or y}")  # Returns True if one of the statements is true
print(f"not x:     {not x}")     # Reverse the result, returns False if the result is true

# 5. Identity Operators
print("\n--- Identity Operators ---")
x1 = ["apple", "banana"]
y1 = ["apple", "banana"]
z1 = x1

# is - Returns True if both variables are the same object
print(f"x1 is z1: {x1 is z1}") # True, because z1 is the same object as x1
print(f"x1 is y1: {x1 is y1}") # False, because x1 and y1 are two different objects, even if they have the same content

# is not - Returns True if both variables are not the same object
print(f"x1 is not y1: {x1 is not y1}") # True

# With simple types like integers, Python often reuses objects, so this can be True:
print(f"5 is 5: {5 is 5}")

# 6. Membership Operators
print("\n--- Membership Operators ---")
x = ["apple", "banana"]
# in - Returns True if a sequence with the specified value is present in the object
print(f"'banana' in x: {"banana" in x}") # True

# not in - Returns True if a sequence with the specified value is not present in the object
print(f"'orange' not in x: {"orange" not in x}") # True

# 7. Bitwise Operators (Advanced)
print("\n--- Bitwise Operators ---")
a = 60 # 60 = 0011 1100
b = 13 # 13 = 0000 1101

print(f"a & b = {a & b}")    # AND
print(f"a | b = {a | b}")    # OR
print(f"a ^ b = {a ^ b}")    # XOR
print(f"~a = {~a}")          # NOT
print(f"a << 2 = {a << 2}") # Zero fill left shift
print(f"a >> 2 = {a >> 2}") # Signed right shift
