import random
import string

def gen_pass(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length):
    passwords = [gen_pass(length) for _ in range(num_passwords)]
    return passwords

def main():
    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        password_length = int(input("Enter the length of each password: "))

        if num_passwords <= 0 or password_length <= 0:
            print("Please enter valid values for number of passwords and password length.")
            return

        gen_pass = generate_multiple_passwords(num_passwords, password_length)

        print("\nGenerated Passwords:")
        for index, password in enumerate(gen_pass, start=1):
            print(f"{password}")

    except ValueError:
        print("Please enter valid numeric values.")

if _name_ == "_main_":
    main()