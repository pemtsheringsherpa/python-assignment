def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            words = contents.split()
            return len(words)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return 0

# Example usage
filename = "sample.txt"
word_count = count_words_in_file(filename)
print(f"The number of words in {filename} is {word_count}.")