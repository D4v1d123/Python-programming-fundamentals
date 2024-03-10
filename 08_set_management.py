# SETS MANAGEMENT
first_semester_subjects = {"Chemitry", "Physical", "Astronomy", "Calculus"}
second_semester_subjects = {"Ethics", "Algebra", "Calculus"}

second_semester_subjects.add("Programming")  # Add an item to the set.
print("Second semester with 'Programming': ", second_semester_subjects)

print("The 'Physical' subject is in the second semester?: ","Physical" in second_semester_subjects)  # Check if a
# data exist in the set. 

# Join two sets
print("All subject of the first and second semester: ", first_semester_subjects.union(second_semester_subjects))

# Check the items that a set has and the other does not.
print("Subject that have first semester and second does not: ", first_semester_subjects.difference(second_semester_subjects)) 

# Check the items that the two sets have in common.
print("The subjects that the two semesters have in common: ", first_semester_subjects.intersection(second_semester_subjects)) 

second_semester_subjects.remove("Algebra")  # Remove a data.
print("'Algebra' subject has been removed: ", second_semester_subjects)

second_semester_subjects.clear()  # Empty a set.
print("The second semester empty: ", second_semester_subjects)
print("\n")