## Suitable for sorted lists. It repeatedly divides the search interval in half until the target value is found.

## Steps:
## Start with the entire sorted list.
## Compute the middle element of the list.
## If the middle element is equal to the target value, return its index.
## If the middle element is less than the target value, search in the right half of the list.
## If the middle element is greater than the target value, search in the left half of the list.
## Repeat steps 2-5 until the target value is found or the search interval is empty.



def binary_search(array: list, target: int, low: int, high: int, loop: int) -> int:
    """
    Performs a binary search recursively to find a target value inside a given list.
    
    Parameters:
        array (list): The sorted list to iterate.
        target (int): The target to find.
        low (int): The lower index of the search interval.
        high (int): The upper index of the search interval.
    
    Returns:
        int: The index of the target value, otherwise -1.
    """
    sorted_array = sorted(array)
    loop += 1
    print(f"Loop  #{loop}")
    print(f"Sorted array : {sorted_array}")
    print(f"Target : {target}")
    print("## Interval ##")
    print(f"Lowest index : {low}")
    print(f"Highest index : {high}")
    if low <= high:
        mid = (low + high) // 2
        print(f"Middle position : {mid}")
        if sorted_array[mid] == target:
            return mid
        elif sorted_array[mid] < target:  # Search right
            return binary_search(array, target, mid + 1, high, loop)
        else:  # Search left
            return binary_search(array, target, low, mid -1, loop)
    else:
        return -1


array = [1, 2, 5, 70, 4 ,25, 10, 42]
target = 42
result = binary_search(array, target, 0, len(array) - 1, 0)

if result != -1:
    print(f"Binary search sucessful: Target found at index {result}")
else:
    print(f"Binary search failed: Target not found!")