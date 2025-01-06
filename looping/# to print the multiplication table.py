#  to print the multiplication table
def multiplication_table(number):
    for i in range(1, 11):
        print(number * i, end=", " if i < 10 else "\n")
number = int(input("Enter a number to generate its multiplication table: "))
multiplication_table(number)
