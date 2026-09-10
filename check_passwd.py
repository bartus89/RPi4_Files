import secrets
import string
import random


# Zestawy znaków
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = "!@#$%^&*_+-="

characters = lowercase + uppercase + digits + symbols


def generate_password(length):
    if length < 8:
        print("\nHasło musi mieć co najmniej 8 znaków!")
        return None

    # Gwarantujemy każdy rodzaj znaku
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    # Pozostałe znaki losowe
    for _ in range(length - 4):
        password.append(secrets.choice(characters))

    # Mieszamy kolejność znaków
    random.SystemRandom().shuffle(password)

    return "".join(password)


def check_password(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in symbols for c in password)

    # Liczymy punkty
    score = sum([
        len(password) >= 12,
        has_upper,
        has_lower,
        has_digit,
        has_symbol
    ])

    levels = {
        0: "Very Weak",
        1: "Weak",
        2: "Weak",
        3: "Medium",
        4: "Strong",
        5: "Very Strong"
    }

    print("\n" + "=" * 45)
    print("             PASSWORD CHECKER")
    print("=" * 45)

    print(f"Długość:           {len(password)}")
    print(f"Wielka litera:     {'TAK' if has_upper else 'NIE'}")
    print(f"Mała litera:       {'TAK' if has_lower else 'NIE'}")
    print(f"Cyfra:              {'TAK' if has_digit else 'NIE'}")
    print(f"Symbol:             {'TAK' if has_symbol else 'NIE'}")
    print(f"\nWynik:              {score}/5")
    print(f"Siła hasła:         {levels[score]}")
    print("=" * 45)


def main():
    while True:
        print("\n" + "=" * 45)
        print("             PASSWORD MANAGER")
        print("=" * 45)
        print("1. Wygeneruj hasło")
        print("2. Sprawdź hasło")
        print("3. Wyjście")
        print("=" * 45)

        choice = input("Wybierz opcję: ").strip()

        if choice == "1":
            try:
                length = int(input("\nPodaj długość hasła: ").strip())

                password = generate_password(length)

                if password:
                    print("\n" + "=" * 45)
                    print("             SECURE PASSWORD")
                    print("=" * 45)
                    print(f"Długość:  {len(password)}")
                    print(f"Hasło:    {password}")
                    print("=" * 45)

                    # Od razu sprawdzamy wygenerowane hasło
                    check_password(password)

            except ValueError:
                print("\nPodaj poprawną liczbę!")

        elif choice == "2":
            password = input("\nPodaj hasło do sprawdzenia: ")

            if password:
                check_password(password)
            else:
                print("\nHasło nie może być puste!")

        elif choice == "3":
            print("\nDo zobaczenia!")
            break

        else:
            print("\nNieprawidłowa opcja. Wybierz 1, 2 lub 3.")


main()