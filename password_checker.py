# Main Password Strength checker function
def password_checker(password):
    length = False
    letters = False
    numbers = False
    symbols = False

    # Is the password longer than eight characters?
    if len(password) > 8:
        length = True
    else: length = False

    # Does the password have numbers?
    numbers = any(char.isdigit() for char in password)
        

    # Does the password have letters?
    letters = any(char.isalpha() for char in password)

    # Does the password have symbols?
    symbols = special_character_checker(password)
            
    print(length)
    print(numbers)
    print(letters)
    print(symbols)

    # Scoring System where 0-2 = "Weak", 3 = "Moderate", and 4 = "Strong"

# Special Character checker function
def special_character_checker(password):
        special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
        '-', '_', '+', '=', '[', ']', '{', '}', ';', ':', ',', '.', '<', '>',
        '/', '?', '\\', '|', '`', '~']
        
        if any(char in special_characters for char in password):
            return True
        else: return False

if __name__ == "__main__":
    password = input("Please enter a password: ")
    password_checker(password)