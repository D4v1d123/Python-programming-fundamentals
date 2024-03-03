# This is a comment

"""
This is a 
multi-line 
comment
"""

'''
This is a 
multi-line
comment
'''

# OUTPUTS
print("Hello world")
print('Hello phyton')

'''
Line breaks in Strings or outputs:
\n => Line break.
\t => Tabulation.
\\n => Skip line break.
\\t => Skip tabulation.
'''

'''
Formatting string in outputs:
%s => String.
%d => Integer.
%f => Floating
%.number of digitsf => Floating point number with fixed precision.
'''
planet_name, planet_number, gravity, size = 'Earth', 3, 9.807, 510.14242544232

print("The {} planet is the {} in the solar system, it has a gravity of {} m/s^2 with a size of {}." . format(planet_name, planet_number, gravity, size))

print("The %s planet is the %d in the solar system, it has a gravity of %f m/s^2 with a size of %.3f." %(planet_name, planet_number, gravity, size) + "\n")


# INPUTS
sum = input("2 + 2 = ")


# VARIABLES
number = 1111  # Int.
decimal = 3.1416  # Float.
complex_number = 3j  # Complex number.
name = "David Guerrero"  # String.
status = True  # Bool.
alphabet = ['a', 'b', 'c', 'd']  # List or array.
phone_numbers = {
    "Alexandra" : 3204527836,
    "Diego" : 3156820913,
    "Mariana" : 3126839756
}  # Dictionary.
salad = {"Tomato", "Salt", "Onion"}  # Set.
city = ("New York", "Bogota", "Mexico city")  # Tuple.

# Variables on a single line (bad practice)
first_name, last_name, age = "Mariana", 'Martinez', 22


# CONSTANTS
PI_NUMBER = 3.1416  # In phyton the constants can be modified. 


'''
Arithmetic operators:
+ => Sum
- => Subtraction
* => Multiplication
/ => Division (10 / 4 = 2.5)
% => Module
** => Exponent
// => Floor division (10 / 4 = 2) => Approximate the result
'''

'''
Comparative operators:
< => Smaller than
> => Greater than
<= => Smaller or equal than
>= => Greater than
== => Iqual than
!= => Different from
'''

'''
Logical operators:
and 
or 
not
'''

'''
Assignment perators:
= => Same to x = 1
+= => Same to x = x + 1 
-= => Same to x = x - 1 
*= => Same to x = x * 1 
/= => Same to x = x / 1 
%= => Same to x = x % 1 
//= => Same to x = x // 1 
**= => Same to x = x ** 1 
'''


# STRING DIVISION
word = "Mexico"

word_slice = word [1 : 5]
print("Mexico [1 : 5] => " + word_slice)

word_slice = word [-1]
print("Mexico [-1] => " + word_slice)

word_slice = word [: -1]
print("Mexico [: -1] => " + word_slice)

word_slice = word [:: -1]
print("Mexico [:: -1] => " + word_slice)

word_slice = word [0 : 6 : 2]
print("Mexico [0 : 6 : 2] => " + word_slice + "\n")


# PHYTON PREDEFINED FUNCTIONS
print("The data type of word is:", type(word)) # Determine the data type.
print("The word length is:", len(word)) # Determine the length of a String.
print("The word is: ", word.capitalize()) # First letter capitalized.
print("The word is: ", word.upper()) # All in capital letters.
print("The word is: ", word.lower()) # All in lower case.
print("The word is capitalized: ", word.isupper()) # Check if a word is capitalized.
print("The 'e' in the Mexico word: ", word.count("e")) # Count how many times a letter is repeated.
print("The word starts with 'Me'?: ", word.startswith("Me")) # Check if a word starts with a specified word.4
print("\n")


# LIST MANAGEMENT
language = ["Phyton", "Swift", "CSS", "JavaScript"]

print("Append 'PHP': ", language.append("PHP"))  # Add an item to the last position.
print("Insert 'HTML' in the second position: ", language.insert(2, "HTML"))  # Add an item at a defined position.
print("The position for 'CSS' is: ", language.index("CSS")) # Identify the index + 1 of an item.
print("Remove 'Phyton':", language.remove("Phyton"))  # Remove a value.

del language[1]  # Remove a value of a defined position.
print("Remove the value of the first position: ", language)

language.reverse()  # Reverse the list
print("Inverted list: ", language)

language.sort()  # Sort the list.
print("Ordered list: ", language)
print("\n")


# QUEUE BEHAVIOR
client = ["Marcela", "Alejandro", "Mariana"]

process = client.pop(0)  # Extract the first item and remove it from the list.
print("Pop: ", process)

client.append("Carlos")  # Add an item to the last position.
print("Add 'Carlos': ", client)
print("\n")


# STACKS BEHAVIOR
client = ["Marcela", "Alejandro", "Mariana"]

process = client.pop()  # Extract the last item and remove it from the list.
print("Pop: ", process)

client.append("Carlos")  # Add an item to the last position.
print("Add 'Carlos': ", client)
print("\n")


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


# CONDITIONALS
condition = True
if condition:  # Simple conditional.
    print("Entered the condition.")

number = 7
if number:  # Simple conditional.
    print("It's a number.")

age = 18
if age >= 18 and age <= 55:  # Simple conditional
    print("It's adult.")
elif age >= 56:  # Optional conditional.
    print("It,s old man or women.")
else:
    print("It's a children.")
print("\n")


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


# FUNCTIONS
# Input arguments or parameters
#               |
#              \/
def sum(number_1, number_2):  # Function with return value.
    return (number_1 + number_2)
#                    /\
#                    |
#      Output arguments or parameters
print("The sum result is: ", sum(1, 2))  # Assign the parameters value in order.
print("The sum result is: ", sum(number_2 = 1, number_1 = 2))  # Assign the value to a specified parameter.

def print_person(name, last_name, nationality = "Colombia"): # Function with optional parameters. 
    print(name, " ", last_name, " is from", nationality)

print_person("David", "Guerrero", "Canada") 
print_person("David", "Guerrero") 

def print_text(*texts):  # Function with dynamic parameters.
    print(texts)

print_text("Hello", "World", "How are you?")
print_text("Hello", "World")
print("\n")


# CLASS
class EmptyPerson:  # Class without attributes.
    pass

class Person:  # Class with attributes.
    def __init__(self, name, last_name, nationality = "Colombia"):  # Constructor method.
        self.nationality = nationality  # Public property.
        self.__full_name = "{} {}" . format(name, last_name)  # Private property.
    #           /\                              /\
    #           |                               |
    #    class attributes               function parameters
    
    def get_full_name (self):  # Get method.
        return self.__full_name

    def walk(self):  # Method 
        print("{} is walking in {}." . format(self.__full_name, self.nationality))

david = Person("David", "Guerrero")  # Instantiate or create a object object of the Person class. 
david.walk()

print("Hi {}." . format(david.get_full_name()))

david.nationality = "Canada"  # Change a value of an attribute of an object.
print("David's nationality is {}." . format(david.nationality))
print("\n")


# EXCEPTIONS HANDLING
number1 = 1
number2 = "2"

print("TRY ONE: ")
try:  # Execute a error-prone code block.
    print("The result of the sum is: {}." . format(number1 + number2))
except Exception as error:  # If a general error happen, execute a code block inside except.
    print("An error has occurred: ({})." . format(error))
else:  # If an error does not happen, execute a code block inside else (Optional).
    print("There are no errors.")
finally:  # Is always executed when there is or is not an error (Optional).
    print("The execution continues.")

print("TRY TWO: ")
try: 
    print("The result of the sum is: {}." . format(number1 + number2))
except ValueError:  # If a specific error happend, execide a code block inside except.
    print("An 'Value Error' error has occurred.")
except TypeError:  # If a specific error happend, execide a code block inside except.
    print("An 'Type Error' error has occurred.")
print("\n")


# MODULES: A module is a set of functionalities dedicated to a same purpose. 
from print import print_greeting  # Import specific functions from a file.
import calculate  # Import all functions from a file.

print_greeting("Mariana")

calculate.sum(5, 7)
calculate.subtract(5, 10)