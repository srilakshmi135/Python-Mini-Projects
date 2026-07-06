import random
import string

print("===== Password Generator =====")

try:
    length = int(input("Enter password length: "))

    if length <= 0:
        print("Password length must be greater than 0.")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("\nGenerated Password:")
        print(password)

except ValueError:
    print("Please enter a valid number.")