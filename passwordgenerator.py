import random
import string

def password_generator():
    length = int(input("Enter the desired length of the password (at least 4 characters): "))

    if length < 4:
        print("Password length should be at least 4 characters.")
        return

    use_uppercase = input("Use uppercase letters? (yes/no): ")
    use_numbers = input("Use numbers? (yes/no): ")
    use_special_chars = input("Use special characters? (yes/no): ")

    all_characters = string.ascii_lowercase

    if use_uppercase.lower() == "yes":
        all_characters += string.ascii_uppercase
    if use_numbers.lower() == "yes":
        all_characters += string.digits
    if use_special_chars.lower() == "yes":
        all_characters += string.punctuation

    password = ''.join(random.choice(all_characters) for i in range(length))

    print("Generated Password: ", password)

    save_password = input("Do you want to save the password? (yes/no): ")

    if save_password.lower() == "yes":
        password_name = input("Enter a name for the password: ")
        with open("passwords.txt", "a") as f:
            f.write(f"{password_name}: {password}\n")
        print("Password saved successfully!")
    else:
        print("Password not saved.")

password_generator()