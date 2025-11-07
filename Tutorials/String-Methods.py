# Python has a set of built-in methods that you can use on strings.

# --- Case Conversion Methods ---
s = "heLLo, AnD weLComE!"
print(f"Original: '{s}'")
print(f"capitalize(): '{s.capitalize()}'") # Converts the first character to upper case
print(f"lower():      '{s.lower()}'")      # Converts a string into lower case
print(f"upper():      '{s.upper()}'")      # Converts a string into upper case
print(f"title():      '{s.title()}'")      # Converts the first character of each word to upper case
print(f"swapcase():   '{s.swapcase()}'")   # Swaps case, lower becomes upper and vice versa

# --- Searching and Finding Methods ---
s = "A long string with long words"
print(f"\nOriginal: '{s}'")
print(f"count('long'): {s.count('long')}") # Returns the number of times a specified value occurs
print(f"find('long'):  {s.find('long')}")  # Searches for a value and returns the position of where it was found
print(f"rfind('long'): {s.rfind('long')}") # Same as find, but searches from the right
print(f"startswith('A'): {s.startswith('A')}") # Returns true if the string starts with the specified value
print(f"endswith('s'):   {s.endswith('s')}")   # Returns true if the string ends with the specified value

# --- Whitespace and Padding Methods ---
s = "   Hello   "
print(f"\nOriginal: '{s}'")
print(f"strip():  '{s.strip()}'")  # Returns a trimmed version of the string
print(f"lstrip(): '{s.lstrip()}'") # Returns a left trim version
print(f"rstrip(): '{s.rstrip()}'") # Returns a right trim version

s = "Python"
print(f"center(10, '-')': '{s.center(10, '-')}'") # Returns a centered string
print(f"ljust(10, '-')':  '{s.ljust(10, '-')}'")  # Returns a left justified version
print(f"rjust(10, '-')':  '{s.rjust(10, '-')}'")  # Returns a right justified version

num = "5"
print(f"zfill(4): '{num.zfill(4)}'") # Pads the string with zeros to fill a total of 4 characters

# --- Splitting and Joining Methods ---
s = "apple,banana,cherry"
print(f"\nOriginal: '{s}'")
print(f"split(','): {s.split(',')}") # Splits the string at the specified separator

lines = "first line\nsecond line\nthird line"
print(f"splitlines(): {lines.splitlines()}") # Splits the string at line breaks

my_tuple = ("John", "Peter", "Vicky")
print(f"'-'.join(my_tuple): '{','.join(my_tuple)}'") # Joins the elements of an iterable to the end of the string

# --- Character Type Checking Methods ---
print("\n--- Character Type Checking ---")
print(f"'Python3'.isalnum(): {'Python3'.isalnum()}") # Returns True if all characters are alphanumeric
print(f"'Python'.isalpha():  {'Python'.isalpha()}")  # Returns True if all characters are in the alphabet
print(f"'12345'.isdigit():   {'12345'.isdigit()}")   # Returns True if all characters are digits
print(f"'   '.isspace():     {'   '.isspace()}")     # Returns True if all characters are whitespaces
print(f"'python'.islower():  {'python'.islower()}")  # Returns True if all characters are lower case
print(f"'PYTHON'.isupper():  {'PYTHON'.isupper()}")  # Returns True if all characters are upper case
print(f"'Hello World'.istitle(): {'Hello World'.istitle()}") # Returns True if the string follows the rules of a title

# --- Replacing Methods ---
s = "I like bananas"
print(f"\nOriginal: '{s}'")
print(f"replace('bananas', 'apples'): '{s.replace("bananas", "apples")}'") # Returns a string where a value is replaced with another

# Advanced replacement with translate
txt = "Hello Sam!"
mytable = str.maketrans("S", "P") # Create a mapping table
print(f"translate(): {txt.translate(mytable)}") # Use the mapping table to replace characters
