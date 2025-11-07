# Simple password strength checker

while True:
    password = input("Please enter your password: ")

    has_int = any(char.isdigit() for char in password)
    has_up = any(char.isupper() for char in password)
    has_low = any(char.islower() for char in password)
    has_sp = any(not char.isalnum() for char in password)
    correct_length = 8 <= len(password) <= 20

    if has_int and has_up and has_low and has_sp and correct_length:
        print("Accepted - Your password meets the parameters")
        break

    if not has_int: # nts use if not >elif when looking for bool
        print("Password must contain at least 1 number.")
    if not has_up:
        print("Password must contain at least 1 uppercase letter.")
    if not has_low:
        print("Password must contain at least 1 lowercase letter.")
    if not has_sp:
        print("Password must contain at least 1 special character.")
    if not correct_length:
        print("Password must be between 8 and 20 characters long.")




