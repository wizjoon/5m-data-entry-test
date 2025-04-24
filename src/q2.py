def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    if not isinstance(lst, list):
        return "Input must be a list."

    return [replace_val if item == find_val else item for item in lst]


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:


# Test 1: [1, 2, 3, 4, 2, 2], 2, 5
# Expected Output: [1, 5, 3, 4, 5, 5]
print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))

# Test 2: ["apple", "banana", "apple"], "apple", "orange"
# Expected Output: ['orange', 'banana', 'orange']
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))

# Test 3: no input list
# Expected Output: Input must be a list.
print(find_and_replace("apple", "apple", "orange"))

# Test 4: ("apple", "banana", "apple"), "apple", "orange", list is a tuple instead of list
# Expected Output: Input must be a list.
print(find_and_replace(("apple", "banana", "apple"), "apple", "orange"))

