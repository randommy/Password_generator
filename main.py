
import secrets
import string


MIN_LENGTH = 8
MAX_LENGTH = 128


def generate_password(length: int) -> str:
    """Generate a cryptographically secure random password."""

    alphabet = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    password = ''.join(
        secrets.choice(alphabet)
        for _ in range(length)
    )

    return password


def get_password_length() -> int:
    """Get and validate password length from user."""

    while True:
        try:
            length = int(input("Enter password length: "))

            if length < MIN_LENGTH:
                print(f"Minimum password length is {MIN_LENGTH}.")
                continue

            if length > MAX_LENGTH:
                print(f"Maximum password length is {MAX_LENGTH}.")
                continue

            return length

        except ValueError:
            print("Invalid input. Please enter an integer.")


def main():
    print("=== SECURE PASSWORD GENERATOR ===")

    length = get_password_length()

    password = generate_password(length)

    print("\nGenerated password:", password)
    print("Password length:", len(password))


if __name__ == "__main__":
    main()
