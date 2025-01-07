def palindrome_check(string):
    # Remove spaces and convert to lowercase for uniformity
    cleaned_string = ''.join(string.split()).lower()
    # Check if the string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

# Example 
test_string = "A man a plan a canal Panama"
if palindrome_check(test_string):
    print(f'"{test_string}" is a palindrome.')
else:
    print(f'"{test_string}" is not a palindrome.')