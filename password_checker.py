# Main password strength checker function

def password_checker(password):
    
    # Does the password contain letters?
    print(f"Your new password is: {password}")


if __name__ == "__main__":
    password = input("Please enter a password: ")
    password_checker(password)