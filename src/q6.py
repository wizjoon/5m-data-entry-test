def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    i = 0
    if lst == []:
        return "List is empty"
    while i < len(lst):
        if lst[i] < 0:
            return lst[i]
        i += 1
    return "No negatives"


# Task 2
# Invoke the function "find_first_negative" using the following scenario:

# Task 1: [3, 5, -1, 7, -2, 8]
# Expected Output: -1
print(find_first_negative([3, 5, -1, 7, -2, 8]))  

# Task 2: [2, 10, 7, 0]
# Expected Output: "No negatives"
print(find_first_negative([2, 10, 7, 0]))         

# Task 3: Empty list
# Expected Output: "List is empty"
print(find_first_negative([]))                    

