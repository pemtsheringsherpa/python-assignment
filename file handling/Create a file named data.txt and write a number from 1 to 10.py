# Create a file named data.txt and write numbers from 1 to 10
with open("data.txt", "w") as file:
    for number in range(1, 10):
        file.write(f"{number}\n")

# Read the file and print its contents
with open("data.txt", "r") as file:
    contents = file.read()
    print(contents)