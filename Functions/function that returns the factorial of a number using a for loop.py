def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result += i
    return result

# Example 
num = 5
print(f"The factorial of {num} is {factorial(num)}.")