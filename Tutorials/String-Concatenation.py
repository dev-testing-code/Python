# String concatenation means joining two or more strings together.

# 1. Using the + operator
a = "Hello"
b = "World"
c = a + b
print(c)  # Output: HelloWorld

# Add a space between them
c = a + " " + b
print(c)  # Output: Hello World

# 2. Using f-Strings (Formatted String Literals)
# This is a modern and often more readable way to concatenate.
a = "Hello"
b = "World"
c = f"{a} {b}"
print(c) # Output: Hello World

# You can also embed expressions directly
print(f"The sum of 2 + 2 is {2 + 2}")

# 3. Using the join() method
# This is the most efficient way to join a large number of strings.
words = ["Hello", "World", "from", "a", "list!"]
sentence = " ".join(words)
print(sentence) # Output: Hello World from a list!

# 4. Using the str.format() method
a = "Hello"
b = "World"
c = "{} {}".format(a, b)
print(c) # Output: Hello World

# You can also use named arguments
c = "{greeting} {name}".format(greeting="Hello", name="World")
print(c) # Output: Hello World
