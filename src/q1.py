def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
   # if x and y is not numeric return -1
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1

    # swap x with y and return x and y
    x, y = y, x
    return x,y


# Task 2
# Invoke the function "swap" using the following scenarios:

# Test 1: "Apple", 10
print("Test 1 Result:", swap("Apple", 10))

# Test 2: 9, 17
print("Test 2 Result:", swap(9, 17))
