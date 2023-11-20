import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if length < 1:
        raise ValueError("Password length must be at least 1.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        # Prompt the user for password length and options
        length = int(input("Enter the desired length of the password: "))
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

        # Generate and display the password
        if length > 0:
            password = generate_password(length, use_digits, use_special_chars)
            print(f"Generated Password: {password}")
        else:
            print("Invalid password length. Please enter a positive integer.")
    except ValueError as e:
        print(f"Error: {e}")
        print("Invalid input. Please enter valid values.")

if __name__ == "__main__":
    main()
