def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if not isinstance(s, str):
        return "Input must be a string"
    else:
        return s[::-1]


# Task 2
# Invoke the function "string_reverse" using the following scenarios:

# Test 1: "Hello World"
# Expected Output: Test 1 Result: dlroW olleH
print("Test 1 Result:", string_reverse("Hello World"))   

# Test 2: "Python"
# Expected Output: Test 2 Result: nohtyP
print("Test 2 Result:", string_reverse("Python"))    

# Test 3: input string str datatype not "string"
# Expected Output: Test 3 Result: Input must be a string
print("Test 3 Result:", string_reverse(12345))           
