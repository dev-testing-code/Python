# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data.
# Lists are created using square brackets.

# 1. Creating a List
print("--- Creating Lists ---")
my_list = ["apple", "banana", "cherry"]
print(f"A simple list: {my_list}")

# Lists can contain different data types
mixed_list = ["abc", 34, True, 40, "male"]
print(f"A mixed-type list: {mixed_list}")

# Using the list() constructor
constructor_list = list(("apple", "banana", "cherry")) # note the double round-brackets
print(f"List from constructor: {constructor_list}")

# 2. Accessing Items
print("\n--- Accessing Items ---")
print(f"First item: {my_list[0]}")
print(f"Last item: {my_list[-1]}")

# Slicing
print(f"Slice [1:3]: {my_list[1:3]}")
print(f"Slice from start [:2]: {my_list[:2]}")
print(f"Slice to end [1:]: {my_list[1:]}")

# 3. Modifying Lists
print("\n--- Modifying Lists ---")
my_list[1] = "blackcurrant"
print(f"After changing an item: {my_list}")

my_list[0:2] = ["watermelon", "orange"]
print(f"After changing a range: {my_list}")

# 4. Adding Items
print("\n--- Adding Items ---")
my_list.append("mango")
print(f"After append('mango'): {my_list}")

my_list.insert(1, "pineapple")
print(f"After insert(1, 'pineapple'): {my_list}")

tropical_fruits = ["papaya", "guava"]
my_list.extend(tropical_fruits)
print(f"After extending with another list: {my_list}")

# 5. Removing Items
print("\n--- Removing Items ---")
my_list.remove("orange")
print(f"After remove('orange'): {my_list}")

popped_item = my_list.pop(1)
print(f"After pop(1): {my_list}, (popped item was '{popped_item}')")

del my_list[0]
print(f"After 'del my_list[0]': {my_list}")

my_list.clear()
print(f"After clear(): {my_list}")

# 6. Looping Through Lists
print("\n--- Looping ---")
new_list = ["a", "b", "c"]
print("Looping with for:")
for x in new_list:
  print(x)

print("\nLooping with range and len:")
for i in range(len(new_list)):
  print(new_list[i])

# 7. List Comprehension
print("\n--- List Comprehension ---")
# A short-hand for creating a new list based on the values of an existing list.
squares = [x**2 for x in range(5)]
print(f"Squares from comprehension: {squares}")

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_fruits = [x for x in fruits if "a" in x]
print(f"Fruits with 'a' in the name: {new_fruits}")

# 8. Sorting and Reversing
print("\n--- Sorting and Reversing ---")
numbers = [100, 50, 65, 82, 23]
print(f"Original numbers: {numbers}")
numbers.sort() # Sorts in-place
print(f"After sort(): {numbers}")
numbers.sort(reverse=True)
print(f"After sort(reverse=True): {numbers}")
numbers.reverse() # Reverses in-place
print(f"After reverse(): {numbers}")

# 9. Copying Lists
print("\n--- Copying Lists ---")
original = [1, 2, 3]
# This does NOT make a copy, it just makes both variables point to the same list
bad_copy = original 

# This makes a true copy
good_copy = original.copy()
# Or like this:
good_copy_2 = list(original)

good_copy[0] = 99
print(f"Original list: {original}")
print(f"Copied list:   {good_copy}")

# 10. Joining Lists
print("\n--- Joining Lists ---")
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(f"Joined with +: {list3}")

list1.extend(list2)
print(f"Joined with extend(): {list1}")
