# DICTIONARIES, HASH MAPS OR MAPS MANAGEMENT: One key only can only have one value or data structure.
grades = {
    "Daniela": 35,
    "Alberto": 40,
    "Freddy": 45,
    "Sofia": 20
}

grades["Jose"] = [30, 40, 20]  # Add a item.
print("All subject notes: ", grades)

del grades["Alberto"]  # Remove a specified item.
print("Grades with 'Alberto'", grades)

print("'Daniela' is in the grades: ", "Daniela" in grades)  # Check if an item exists within the dictionary.
print("All keys or names in the grades: ", grades.keys())  # Extract all keys of the dictionaries.
print("All values in the grades: ", grades.values())  # Extract all values of the dictionaries.
print("Dictionary created without values: ", dict.fromkeys(["Daniela", "Alberto", "Freddy"]))  # Create a new 
# dictionary with the specified keys and without values. 

print("Dictionary created without values based on 'grades': ", dict.fromkeys(grades))  # Create a new dictionary
# without values based on another dictionary.

print("Dictionary created with the value '50' and the 'grades' keys: ", dict.fromkeys(grades, 50))  # Create a 
# new dictionary with the specified value and based on another dictionary.
print("\n")