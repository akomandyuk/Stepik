# Type a string of some words
# Lowercase all of them
# Create a list with every single word as a list element
lst = input("Type your words: ").lower().split()

# For every element in a list count how many times we found it
# Create a dictionary 'my_dict' with a key 'i' and value 'list.count(i)'
# For example: key 'lollipops': value '3'
my_dict = {i: lst.count(i) for i in lst}

# Go through the entire dictionary
# Print 1 key: value pair in one line
# Move to the next line
for key, value in my_dict.items():
    print(key, value, end='\n')


