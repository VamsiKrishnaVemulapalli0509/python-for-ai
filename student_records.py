student = {
    "name": "Vemulapalli Vamsi Krishna",
    "age": 28,
    "city": "Hyderabad",
    "course": "AI mastery"
}

# Added key
student["Institution"] = "FLM"


# Updated age
student["age"] = 29

# Updated status
student["status"] = "graduated"

# Value removed using pop()
removed_city = student.pop("city")

print(student)
print(student.keys())
print(student.values())
print(student.items())

students = {
    "student1": {"name": "Vamsi", "grade": "A"},
    "student2": {"name": "Krishna", "grade": "B"}
}

# Student selected
print(students["student2"]["name"])

# Original grade
print(students["student2"]["grade"])

# Updated grade
updated_students=students["student2"]["grade"] = "A+"

print(updated_students)
