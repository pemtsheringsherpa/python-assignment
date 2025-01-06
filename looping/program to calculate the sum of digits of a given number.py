
num = input("Enter a number: ")

# initialize sum to 0
sum_of_digits = 0

for digit in num:
    sum_of_digits += int(digit)
    
print(f"The sum of the digits of {num} is {sum_of_digits}.")