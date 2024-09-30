# TERNARY CONDITIONAL OPERATOR: It is the action of assigning the value to a 
# variable with respect to a condition, this improves readability because the code
# is written in one line. It tool is used for simple operations.
age = int(input("Write your age: "))

# Variable.       Condition. 
#   ↓                 ↓
id_type = "CC" if age >= 18 else "TI"#⭠ Value if the condition is False.
#          ↑                      
# Value if the condition is True.

print(f"Your id type is {id_type}")