import secrets
import string


MIN_LENGTH = 8
MAX_LENGTH = 128

def gen_password(
    length: int,
    use_uppercase: bool,
    use_lowercase: bool,
    use_digits: bool,
    use_symbols: bool
) -> str:
    """Generate a password using selected character"""

    alphabet = ""

    if use_uppercase:
        alphabet += string.ascii_uppercase

    if use_lowercase:
        alphabet += string.ascii_lowercase

    if use_digits:
        alphabet += string.digits

    if use_symbols:
        alphabet += string.punctuation

    password = ''.join(
        secrets.choice(alphabet)
        for _ in range(length)
    )

    return password


def get_password_length() -> int:

    while True:
        try:
            length = int(input("Enter password length ---->> "))

            if length < MIN_LENGTH:
                print(f"Minimum password length -->> {MIN_LENGTH}.")
                continue

            if length > MAX_LENGTH:
                print(f"Maximum length is {MAX_LENGTH}.")
                continue

            return length

        except ValueError:
            print("Invalid!!  Pls enter an integer!")


def options() -> tuple[bool, bool, bool, bool]:

    print("\n<<< CHARACTER SELECTION =>>")
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
    use_digits = input("Include digits? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    if not any((use_uppercase, use_lowercase, use_digits, use_symbols)):
        print("Select at least one character type")
        return options()

    return (
        use_uppercase,
        use_lowercase,
        use_digits,
        use_symbols
    )


def main():
    print("\n=== PASSWORD GENERATOR ===")
    length = get_password_length()
    opt1ons = options()
    password = gen_password(length, *opt1ons)
    print("\nGenerated password:", password)
    print("Password length:", len(password))


if __name__ == "__main__":
    main()