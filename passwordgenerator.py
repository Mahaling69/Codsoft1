import random
import string

def generate_password(length):
    # Define the characters to use for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password using random.choice
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Prompt the user for the desired password length
try:
    length = int(input("Enter the desired password length: "))
    if length <= 0:
        print("Password length must be greater than 0.")
    else:
        password = generate_password(length)
        print("Generated Password:", password)
except ValueError:
    print("Invalid input. Please enter a valid number for the password length.")
    
