# MODULES: A module is a set of functionalities dedicated to a same purpose. 
from modules.print import print_greeting  # Import specific functions from a file.
import modules.calculate as calculate  # Import all functions from a file.

print_greeting("Mariana")

calculate.sum(5, 7)
calculate.subtract(5, 10)