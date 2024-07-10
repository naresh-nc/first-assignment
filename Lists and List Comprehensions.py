# Create a list of your favorite fruits.
# Use a list comprehension to create a new list containing the lengths of each fruit.
# Append a new fruit to the original list.
# Sort the list alphabetically.


# Favorite fruits
fruits = ["apple", "banana", "orange"]

# Lengths using list comprehension
fruit_lengths = [len(fruit) for fruit in fruits]
print("lenth of each fruit",fruit_lengths)

# Append a new fruit
fruits.append("mango")
print("Adding new fruit in list", fruits)

# Sort fruits alphabetically
fruits.sort()
print("List after sorting", fruits)