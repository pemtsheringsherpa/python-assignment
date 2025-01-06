
def reverse_string(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string

input_string = "Pema"
output_string = reverse_string(input_string)
print("Input:", input_string)
print("Output:", output_string)