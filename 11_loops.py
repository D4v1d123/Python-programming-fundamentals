# LOOPS
# break => Stops the execution of a loop
# continue => Skip a loop iteration
condition = 0
while condition < 5:  # Execute one or more times a block of code.
    print("while:", condition)
    condition += 1
else:  # It's optional.
    print("'condition' is greater than or equal to 5.")

student_list = ["Yesid", "Alejandro", "Mariana", "Jessica"]
print("The students list are: ")
for student in student_list: # Iterate a list of items
    print(student)
else:
    print("There are no students.")
print("\n")