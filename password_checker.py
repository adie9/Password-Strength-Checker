# Main password strength checker function

def password_checker(password):
    length = False
    letters = False
    numbers = False

    # Is the password longer than eight characters?
    if len(password) > 8:
        length = True
    else: length = False


    # Does the password have numbers?
    numbers = any(char.isdigit() for char in password)
        

    # Does the password have letters?
    letters = any(char.isalpha() for char in password)
            
    print(length)
    print(numbers)
    print(letters)

    # Scoring System where 0-2 = "Weak", 3 = "Moderate", and 4 = "Strong"


if __name__ == "__main__":
    password = input("Please enter a password: ")
    password_checker(password)