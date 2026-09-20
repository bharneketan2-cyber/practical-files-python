# Tuple operations
t = (10, 20, 30, 40)
print("Tuple element:", t[1])

# Set operations
s = {1, 2, 3, 4}
s.add(5)
s.remove(2)
print("Set:", s)

# Dictionary operations
student = {"name": "Amit", "age": 20, "marks": 85}

print("Name:", student["name"])

student["marks"] = 90
student["city"] = "Nagpur"
del student["age"]

print("Updated Dictionary:", student)
print("Dictionary Keys:", student.keys())
print("Dictionary Values:", student.values())
print("Dictionary Items:", student.items())