def add_to_total(current_total, amount):
    new_total = current_total + amount
    return new_total

total = 0
total = add_to_total(total, 10)
total = add_to_total(total, 20)

print("Final total:", total)

def greet():
    print("Hello!")

greet   #  Missing parentheses, function not executed

def greet():
    print("Hello!")

greet()  # Function is called properly

def say_hello()   #  Missing colon
    print("Hello!")

def say_hello():  #  Colon added
    print("Hello!")


def add_numbers(a, b):
print(a + b)   #  Not indented inside function


def add_numbers(a, b):
    print(a + b)   #  Proper indentation
