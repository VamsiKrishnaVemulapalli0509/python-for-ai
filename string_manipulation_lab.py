# Profile Output
full_name = "Vamsi"

# Concatenation
greeting = "Hello " + full_name

# f-string
introduction = f"My name is {full_name}, I love Python."

print("Greeting:", greeting)
print("Introduction:", introduction)

# Part 3 — Text Cleaning
raw1 = " Python Learner "
cleaned1 = raw1.strip().title()

raw2 = "$19.99"
cleaned2 = raw2.lstrip("$")

print("Cleaned 1:", cleaned1)
print("Cleaned 2:", cleaned2)

# Part 4 — Text Search Results
message = "I love Python programming with Python"

membership = "Python" in message
prefix = message.startswith("I")
suffix = message.endswith("Python")
index_find = message.find("Python")
occ_count = message.count("Python")

print("Membership Search:", membership)
print("Prefix Check:", prefix)
print("Suffix Check:", suffix)
print("Index Find:", index_find)
print("Occurrence Count:", occ_count)

# Part 5 — Replacement
original = "I love Python programming with Python"
replaced = original.replace("Python", "AI")

print("Original Message:", original)
print("After Replacement:", replaced)