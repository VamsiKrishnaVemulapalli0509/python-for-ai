def banner(course_title):
    print("===================================")
    print(f" Welcome to {course_title} ")
    print("===================================")

def greet_student(name):
    print(f"Hello, {name}! Ready to learn?")

def square_number(x):
    return x * x

def cube_number(x):
    return x * x * x

def practice_run():
    banner("Python course")
    banner("Ai Mastery")
    greet_student("Vamsi")
    greet_student("Krishna")

    print("Square of 6:", square_number(6))
    print("Cube of 4:", cube_number(4))
    print("Square of 9:", square_number(9))
    print("Cube of 2:", cube_number(2))

practice_run()