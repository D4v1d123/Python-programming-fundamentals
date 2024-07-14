# CALLABLES => These are objects that can be called or invoked through parentheses, 
# this includes function, methods, and classes that implement the __call__ magic 
# method.
def greet(name):
    print(f"Hello {name}!!!")
    
class Dog:
    def __init__(self, name, age, sex):
        self.name = name,
        self.age = age,
        self.sex = sex
        
    def walk(self):
        print(f"The dog {self.name} is walking.")
        
class Counter:
    def __init__(self, start=0):
        self.start = start
        
    def __call__(self): # Magic method that makes a class simulate the behavior of 
                        # a function.
        self.start += 1
    
lambda_function = lambda name : print(f"Hello {name}, I am a lambda function")
dog_1 = Dog("anastacio", 6, "male")

print("IS A CALLABLE?:")       
print(f"* Greet function: {callable(greet)}. \
      \n* Anonymous or lambda function: {callable(lambda_function)}. \
      \n* Walk method: {callable(Dog.walk)}. \
      \n* Dog class: {callable(Dog)}. \
      \n* dog_1 object: {callable(dog_1)}. \
      \n* Counter class: {callable(Counter)}.")
        
# callable() => Function that determines whether an object is callable (True) or not
# (False). It is very useful to check if the arguments of a function or method are
# callable objects in order to handle errors effectively.
def operate_numbers(func, list):
    if not callable(func): # Check if func object is a callable.
        print(f"ERROR: \"{func}\" is not a function.")
    else:
        result = []
        for number in list:
            result.append(func(number))
            
        return result
            
def square_numbers(number):
    return number ** 2

var = "variable"
numbers_list = [1, 2, 3, 4, 5]

print("\nRESULTS:")
print(f"* With \"var\": {operate_numbers(var, numbers_list)}. \
      \n* With \"square_numbers\": {operate_numbers(square_numbers, numbers_list)}.")