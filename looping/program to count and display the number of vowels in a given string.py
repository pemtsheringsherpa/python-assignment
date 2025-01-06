def count_vowels(input_string):
    # Define a set of vowels (both lowercase and uppercase)
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    vowel_count = 0
    for char in input_string:
        if char in vowels:
            vowel_count += 1

    return vowel_count

user_input = input("Enter a string: ")

vowel_count = count_vowels(user_input)

print(f"The number of vowels in the string is: {vowel_count}")
