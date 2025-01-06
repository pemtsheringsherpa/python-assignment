def find_largest_and_smallest(numbers):
    if not numbers:
        return None, None

    largest = numbers[0]
    smallest = numbers[0]

    for number in numbers[1:]:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

    return largest, smallest

# Example usage
numbers = [3, 5, 1, 2, 4, 8, 7]
largest, smallest = find_largest_and_smallest(numbers)
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")