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
except ValueError:  # If a specific error happen, execute a code block inside except.
    print("An 'Value Error' error has occurred.")
except TypeError:  # If a specific error happen, execute a code block inside except.
    print("An 'Type Error' error has occurred.")
print("\n")