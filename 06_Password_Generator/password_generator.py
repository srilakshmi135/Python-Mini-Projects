import random
import string

print("===== Strong Password Generator =====")

try:
    length = int(input("Enter password length (minimum 4): "))

    if length < 4:
        print("Password length must be at least 4.")

    else:
        password = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]

        characters = string.ascii_letters + string.digits + string.punctuation

        for i in range(length - 4):
            password.append(random.choice(characters))

        random.shuffle(password)

        final_password = ""

        for ch in password:
            final_password += ch

        print("\nGenerated Strong Password:")
        print(final_password)

except ValueError:
    print("Please enter a valid number.")