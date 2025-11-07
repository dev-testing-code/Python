# Booleans represent one of two values: True or False.

# 1. Boolean Values
# Booleans are the result of comparison operations.
print(10 > 9)    # Output: True
print(10 == 9)   # Output: False
print(10 < 9)    # Output: False

# 2. The bool() Function
# The bool() function allows you to evaluate any value, and give you True or False in return.

# Most values are True
print(bool("Hello"))
print(bool(15))
print(bool(["apple", "cherry"]))

# Some values are False (these are called "Falsy" values)
print(f"bool(False) is {bool(False)}")
print(f"bool(None) is {bool(None)}")
print(f"bool(0) is {bool(0)}")
print(f'bool("") is {bool("")}')          # Empty string
print(f"bool(()) is {bool(())}")          # Empty tuple
print(f"bool([]) is {bool([])}")          # Empty list
print(f"bool({{}}) is {bool({})}")       # Empty dictionary

# 3. Booleans in Conditional Logic
# Booleans are most often used in if statements.
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# 4. Boolean Operators: and, or, not
x = 5
y = 10

# and - returns True if both statements are true
print(x > 0 and y > 0) # Output: True

# or - returns True if one of the statements is true
print(x > 0 or y < 0) # Output: True

# not - reverses the result, returns False if the result is true
print(not(x > 0 and y > 0)) # Output: False

# 5. Functions can return a Boolean
def is_even(number):
    return number % 2 == 0

print(f"Is 10 even? {is_even(10)}")
print(f"Is 7 even? {is_even(7)}")

# 6. `is` vs `==` with Booleans
# For the boolean values True and False, `is` and `==` work the same way
# because there is only one instance of True and one instance of False.
print(True == 1) # True, because 1 is a "truthy" value
print(True is 1)  # False, because they are different objects in memory

print(True is bool(1)) # True