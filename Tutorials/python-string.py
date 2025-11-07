# String literals
single_quoted_string = 'hello'
double_quoted_string = "world"
triple_quoted_string = """
This is a multi-line
string.
"""

# String concatenation
greeting = single_quoted_string + " " + double_quoted_string
print(greeting)  # Output: hello world

# String formatting (f-strings)
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)

# String methods
s = "  Hello, World!  "
print(s.upper())  # Output: "  HELLO, WORLD!  "
print(s.lower())  # Output: "  hello, world!  "
print(s.strip())  # Output: "Hello, World!"
print(s.replace("World", "Python"))  # Output: "  Hello, Python!  "
print(s.split(","))  # Output: ['  Hello', ' World!  ']

# Slicing and indexing
s = "Python"
print(s[0])  # Output: 'P'
print(s[-1])  # Output: 'n'
print(s[2:5])  # Output: 'tho'
print(s[:2])  # Output: 'Py'
print(s[2:])  # Output: 'thon'

# String length
print(len(s))  # Output: 6

# --- Advanced Concepts ---

# String Immutability
# Strings are immutable, meaning they cannot be changed after creation.
# Any operation that seems to modify a string actually creates a new one.
my_string = "hello"
# The following line would raise a TypeError:
# my_string[0] = 'H' 
new_string = my_string.replace('h', 'H')
print(my_string)   # Output: hello
print(new_string)  # Output: Hello

# Efficient String Joining
words = ["Python", "is", "awesome"]
# Inefficient way for many strings:
inefficient_sentence = ""
for word in words:
    inefficient_sentence += word + " "
# Efficient way:
efficient_sentence = " ".join(words)
print(efficient_sentence) # Output: Python is awesome

# Advanced Formatting with str.format()
person = {'name': 'Bob', 'age': 42}
formatted_person = "Name: {p[name]}, Age: {p[age]}".format(p=person)
print(formatted_person)

# Regular Expressions (Regex)
import re
text = "The rain in Spain"
# Find all occurrences of "ai"
matches = re.findall("ai", text)
print(matches)  # Output: ['ai', 'ai']

# Search for the first white-space character in the string
search = re.search("\s", text)
if search:
    print(f"First white-space character found at position: {search.start()}")

# Unicode and Encoding
# Python strings are Unicode by default. To send them over a network or save to a file,
# you often need to encode them into bytes.
unicode_string = "你好, world"
encoded_utf8 = unicode_string.encode('utf-8')
print(encoded_utf8) # Output: b'\xe4\xbd\xa0\xe5\xa5\xbd, world'

decoded_string = encoded_utf8.decode('utf-8')
print(decoded_string == unicode_string) # Output: True