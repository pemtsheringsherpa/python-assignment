def get_integer_input():
    try:
        user_input = int(input("Please enter an integer: "))
    except ValueError:
        print("Invalid input, please enter an integer.")
    else:
        print(f"You entered the integer: {user_input}")

# Example
get_integer_input()