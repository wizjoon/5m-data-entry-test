def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    if key in dct:
        print(f"Original value for '{key}': {dct[key]}")
    dct[key] = value
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:


# Test 1: {}, "name", "Alice"
# Expected Output - Updated Dictionary 1: {'name': 'Alice'}
result = update_dictionary({}, "name", "Alice")
print("Updated Dictionary 1:", result)                              

# Test 2: {"age": 25}, "age", 26
# Expected Output - Updated Dictionary 2: {'age': 26}  
result = update_dictionary({"age": 25}, "age", 26)
print("Updated Dictionary 2:", result)                                                            


