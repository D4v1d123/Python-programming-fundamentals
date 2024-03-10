# LIST MANAGEMENT
language = ["Python", "Swift", "CSS", "JavaScript"]

print("Append 'PHP': ", language.append("PHP"))  # Add an item to the last position.
print("Insert 'HTML' in the second position: ", language.insert(2, "HTML"))  # Add an item at a defined position.
print("The position for 'CSS' is: ", language.index("CSS")) # Identify the index + 1 of an item.
print("Remove 'Python':", language.remove("Python"))  # Remove a value.

del language[1]  # Remove a value of a defined position.
print("Remove the value of the first position: ", language)

language.reverse()  # Reverse the list
print("Inverted list: ", language)

language.sort()  # Sort the list.
print("Ordered list: ", language)
print("\n")