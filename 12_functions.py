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