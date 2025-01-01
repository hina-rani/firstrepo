def describe (**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe(name="Alice", age=25)
# Output:
#name: Alice
#age: 25