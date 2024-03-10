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
print('Hello python')

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

print("The {} planet is the {} in the solar system, it has a gravity of {} m/s^2 "
"with a size of {}." . format(planet_name, planet_number, gravity, size))
print("The %s planet is the %d in the solar system, it has a gravity of %f m/s^2 "
"with a size of %.3f." %(planet_name, planet_number, gravity, size) + "\n")


# INPUTS
sum = input("2 + 2 = ")