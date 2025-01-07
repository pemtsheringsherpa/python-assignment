def find_max(lst):
    if not lst:
        return None
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value

# Example usage
numbers = [3, 5, 7, 2, 8, 1]
print(f"The maximum value in the list is {find_max(numbers)}.")