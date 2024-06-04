# EXPRESSION: It is a call to a function, value, variable, or comparison that returned 
# a value when executed.
def addition(num1, num2):
    return num1 + num2

print("EXPRESSIONS:")
print(1 != 3)  # => Comparison that returns True.
print(addition(2, 2))  # => Call to a function that returns 4.
print(name := "Natalia Olgado Cabello", end="\n\n")  # => Assignment to a variable that returns it's value.

# STATEMENT: Is an instruction that performs an action, and when executed does not
# necessarily return a value. A statement can be made up of one or most expression.
brands = ["Porche", "Koenigsegg", "Aston Martin"]

print("STATEMENT:")
print(brands.append("Bentley"), end="\n\n")  # => Statement

# WALRUS OPERATOR: It allow assign a value to a variable within a condition and 
# then use it. In some cases, depending on the context, the Walrus operator reduce 
# the code duplicity, thus improving the readability and performance of the software. 
# This operator is an expression and should always be used between parenthesis. 
from functools import reduce 

student_grades = {
    "Gabriela García Pérez de la Fuente" : [3.5, 4, 4.3, 1, 3],
    "Carlos Mendoza López Rodríguez" : [2.4, 3.8, 5, 2],
    "Ana Rodríguez Jiménez de la Cruz" : [],
    "Luis Fernández Gómez Sánchez" : [5, 4.8, 4.9, 3.7],
    "María López Castillo Morales" : [4.2, 3.5, 3.9, 2.6, 5]
}

print("WALRUS OPERATOR:")
for name, grades in student_grades.items():
    # Walrus operator (return the value assigned or len(grades) to be evaluate with 4).
    #                  ↓
    if (number_grades := len(grades)) >= 4:
        #                      Sum of all grades student / Number of grades.
        final_grade = reduce(lambda x, y: x + y, grades) / number_grades
        print(f"* {name} = {final_grade}")
    else:
        print(f"* {name} = !!! {4 - number_grades} grade/s missing. !!!")