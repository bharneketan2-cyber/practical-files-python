# Program 3: User-defined Module Concept
# Step 1: Create file my_module.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
# Step 2: Import and use module
import my_module

print("Addition:", my_module.add(5, 3))
print("Multiplication:", my_module.multiply(4, 2))
