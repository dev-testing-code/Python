# Although strings are immutable, you can create new strings based on modifications of old ones.

# Uppercase
s = "Hello, World!"
print(s.upper())  # Output: HELLO, WORLD!

# Lowercase
s = "Hello, World!"
print(s.lower())  # Output: hello, world!

# Remove Whitespace (strip)
# strip() removes leading and trailing whitespace
s = "  Hello, World!  "
print(s.strip())  # Output: "Hello, World!"

# lstrip() and rstrip() remove only leading or trailing whitespace respectively
print(s.lstrip()) # Output: "Hello, World!  "
print(s.rstrip()) # Output: "  Hello, World!"

# Replace String
s = "Hello, World!"
print(s.replace("H", "J"))     # Output: Jello, World!
print(s.replace("World", "Python")) # Output: Hello, Python!

# Split String
# The split() method returns a list where the text between the specified separator becomes the list items.
s = "Hello, World!"
print(s.split(","))  # Output: ['Hello', ' World!']

# Join Strings
# The join() method takes all items in an iterable and joins them into one string.
my_list = ['Hello', 'World']
print(" ".join(my_list)) # Output: Hello World
print(",".join(my_list)) # Output: Hello,World
