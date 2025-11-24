import random
import string

def generate_password(length=12, use_digits=True, use_symbols=True):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    characters = letters
    if use_digits:
        characters += digits
    if use_symbols:
        characters += symbols

    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("=== PASSWORD GENERATOR ===")

    try:
        length = int(input("Enter password length (e.g., 12): "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_digits, use_symbols)
    print("\nGenerated Password:")
    print(password)

if __name__ == "__main__":
    main()
