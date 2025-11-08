import random
import string

def generate_password(length, use_uppercase=True, use_numbers=True, use_symbols=True):
    # Basic character set (lowercase letters)
    characters = string.ascii_lowercase

    # Add other character sets based on user preferences
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("🔐 Welcome to the Random Password Generator 🔐")
    print("-" * 50)

    # Get password length
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a number.")

    # Ask for character preferences
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    # Generate and display the password
    password = generate_password(length, use_uppercase, use_numbers, use_symbols)

    print("\n✅ Your Secure Password is:")
    print(password)
    print("-" * 50)


if __name__ == "__main__":
    main()