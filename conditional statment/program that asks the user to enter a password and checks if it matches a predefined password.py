# Predefined password
predefined_password = "Pema sherpa"

# Prompt the user to enter a password
user_password = input("Enter the password: ")

if user_password == predefined_password:
    print("Access granted!")
else:
    print("Access denied. Incorrect password.")
