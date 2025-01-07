def open_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

# Example 
filename = "unknown.txt"
open_file(filename)