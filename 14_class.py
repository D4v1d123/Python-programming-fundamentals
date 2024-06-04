# CLASS
class EmptyPerson:  # Class without attributes.
    pass

class Person:  # Class with attributes.
    def __init__(self, name, last_name, nationality = "Colombia"):  # Constructor method.
        self.nationality = nationality  # Public property.
        self.__full_name = "{} {}" . format(name, last_name)  # Private property.
    #            ↑                              ↑
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