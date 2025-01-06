def sum_of_evens(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0: 
            total += num
    return total

# Example
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_of_evens(numbers)
print(f"The sum of all even numbers in the list is: {result}")
