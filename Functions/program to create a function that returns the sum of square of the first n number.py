def sum_of_squares(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 2
    return sum

# Example usage
n = 5
print(f"The sum of squares of the first {n} natural numbers is {sum_of_squares(n)}.")