import random
import string

def generate_password(length=12, complexity='medium'):
    if complexity == 'low':
        characters = string.ascii_letters
    elif complexity == 'medium':
        characters = string.ascii_letters + string.digits
    elif complexity == 'high':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity. Using medium complexity.")
        characters = string.ascii_letters + string.digits

    
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Input for password length
length = int(input("Enter the desired length of the password: "))

# Input for password complexity
complexity = input("Enter the complexity (low, medium, high): ").lower()

# Generate the password based on user input
password = generate_password(length, complexity)
print("Generated Password:", password)
