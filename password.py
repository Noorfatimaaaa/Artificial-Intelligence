#14. Password Validation:
password = input("Enter password: ")

lower = False
upper = False
digit = False
special = False

for character in password:

    if character >= 'a' and character <= 'z':
        lower = True

    elif character >= 'A' and character <= 'Z':
        upper = True

    elif character >= '0' and character <= '9':
        digit = True

    elif character == '$' or character == '#' or character == '@':
        special = True

if len(password) >= 6 and len(password) <= 16 and lower and upper and digit and special:
    print("Valid Password")
else:
    print("Invalid Password")
