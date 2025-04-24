def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """

    if isinstance(num, (int, float)) and isinstance(divisor, (int, float)):
        if divisor == 0 or num == 0:
            return False  # Prevent division by zero
        return num % divisor == 0
    else:
        return False

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:


# Test 1: 10, 2
print(check_divisibility(10, 2))  # Expected output: True

# Test 2: 7, 3
print(check_divisibility(7, 3))   # Expected output: False

# Test 3: num = 0
print(check_divisibility(7, 0))   # Expected output: False

# Test 4: divisor = 0
print(check_divisibility(0, 3))   # Expected output: False


# Test 5: num is not a number
print(check_divisibility("a", 3))   # Expected output: False

# Test 6: divisor is not a number
print(check_divisibility(10, "a"))   # Expected output: False

