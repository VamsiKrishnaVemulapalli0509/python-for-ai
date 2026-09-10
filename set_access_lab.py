empty_set = set()
empty_dict = {}

print("type(set()):", type(empty_set))
print("type({}):", type(empty_dict))

signup_list = ["alice", "bob", "alice", "charlie", "bob", "diana"]
unique_users = set(signup_list)

print("Original Entry Count:", len(signup_list))
print("Unique User Collection:", unique_users)
print("Unique Count:", len(unique_users))

unique_users.remove("alice")      # removes alice
unique_users.discard("unknown_user")  # safe discard

print("After remove/discard:", unique_users)

print("alice in users?", "alice" in unique_users)
print("diana in users?", "diana" in unique_users)

print("Printed Set:", unique_users)
print("Printed List:", list(unique_users))

tags = ["python", "ai", "python", "ml", "data"]
unique_tags = set(tags)

print("Original Tag Entry Count:", len(tags))
print("Unique Tags Set:", unique_tags)
print("Does 'python' exist?", "python" in unique_tags)

unique_tags.add("deep_learning")
unique_tags.discard("ml")

print("Final Unique Tag Set:", unique_tags)