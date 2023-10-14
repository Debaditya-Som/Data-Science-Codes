import string
import getpass

def check_password_strength(password):
    strength = 0
    remarks = []

    if len(password) < 8:
        remarks.append("Password is too short. It should be at least 8 characters long.")
    if any(c in string.ascii_lowercase for c in password):
        strength += 1
    if any(c in string.ascii_uppercase for c in password):
        strength += 1
    if any(c in string.digits for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1

    if strength == 1:
        remarks.append("That's a weak password. Consider using a mix of character types.")
    elif strength == 2:
        remarks.append("Your password is okay, but it can be improved.")
    elif strength >= 3:
        remarks.append("Your password is strong.")

    return remarks

def main():
    print('Welcome to Password Strength Checker')
    while True:
        password = getpass.getpass('Enter the password: ')
        strength_remarks = check_password_strength(password)
        for remark in strength_remarks:
            print(remark)

        choice = input('Do you want to check another password\'s strength (y/n): ')
        if choice.lower() != 'y':
            print('Exiting...')
            break

if __name__ == '__main__':
    main()
