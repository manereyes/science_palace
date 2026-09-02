## Checks every element sequentially until if finds the target value

## Steps:
## Start from the first element of the list.
## Compare each element of the list with the target value.
## If the element matches the target value, return its index.
## If the target value is not found after iterating through the entire list, return -1.



def linear_search(array: list, target: int) -> int:
    """
    Performs a linear search over a given list to find a given target.
    
    Parameters:
        array (list): The list to be iterated.
        target: The value to search for.
        
    Returns:
        int: The index of the found value inside the array, otherwise, returns -1
    """
    
    print("### Initiate Linear Search ###")
    print(f"array : {array}")
    print(f"target: {target}")
    
    for i in range(len(array)):
        print(f"Index: {i} - Value: {array[i]}")
        if array[i] == target:
            return i
    return -1

array = [1, 2, 5, 70, 4 ,25, 10, 42]
target = 4

result = linear_search(array, target)

if result != -1:
    print(f"Linear search sucessful: Target found at index {result}")
else:
    print(f"linear search failed: Target not found!")