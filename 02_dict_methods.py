marks = {
    "Rudra" : 99,
    "Peter" : 65,
    "Kent" : 45,
    "list" : [1, 2, 3],
    0 : "Spiderman" # This is also possible
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Rudra" : 100, "Ironman" : 99}) # We can add new keys if there is nothing in the first
print(marks)

# print(marks.get("Rudra")) Returns Same Value
# print(marks["Rudra"]) Returns Same Value

# print(marks.get("Rudra2")) # Gives None
# print(marks["Rudra2"]) # Returns an error

user = {"name": "Alice", "age": 25, "role": "Admin"}
print(user)

# Example 1: Popping an existing key
role_value = user.pop("role")
print(role_value)  # Output: Admin
print(user)        # Output: {'name': 'Alice', 'age': 25}

# Example 2: Handling a missing key safely with a default value
country = user.pop("country", "Not Found")
print(country)     # Output: Not Found (No error raised!)

# Create a sample dictionary
profile = {"username": "coder12", "status": "active", "points": 450}
print(profile)

# Example 1: Popping the last inserted item
last_item = profile.popitem()
print(last_item)  # Output: ('points', 450)
print(profile)    # Output: {'username': 'coder12', 'status': 'active'}

# Example 2: Unpacking the tuple directly
key, value = profile.popitem()
print(f"Removed Key: {key}, Removed Value: {value}")
# Output: Removed Key: status, Removed Value: active