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

    # Does the password have letters?
    letters = any(char.isalpha() for char in password)
    
    # Does the password have numbers?
    numbers = any(char.isdigit() for char in password)
    
    # Does the password have symbols?
    symbols = special_character_checker(password)

    # Assign categories to list
    category_list = [length, letters, numbers, symbols]

    password_strength = score_calculator(category_list)
    print(f"Your password strength is: {password_strength}")
            
    
# Scoring System where 0-2 = "Weak", 3 = "Moderate", and 4 = "Strong"
def score_calculator(categories):
    score = 0

    for cat in categories:
        if cat == True:
            score += 1
    
    # Calculate score
    if score < 3:
        return "Weak"
    elif score == 3:
        return "Moderate"
    elif score == 4:
        return "Strong"
    
    

# Special Character checker function
def special_character_checker(password):
        special_characters = [' ', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
        '-', '_', '+', '=', '[', ']', '{', '}', ';', ':', ',', '.', '<', '>',
        '/', '?', '\\', '|', '`', '~']
        
        if any(char in special_characters for char in password):
            return True
        else: return False

if __name__ == "__main__":
    password = input("Please enter a password: ")
    password_checker(password)