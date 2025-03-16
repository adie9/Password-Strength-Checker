# Python Password Strength Checker

This project entails creating a simple password strength checker using Python.

## Overview

I began with creating the main function of the project, "password_checker".

```python
def password_checker(password):
    length = False
    letters = False
    numbers = False
    symbols = False
```

The four variables are the categories for the scoring system to be implemented. In the future, I would like to add more complexity to them. The values are set to "False" by default.

Next, I set conditions for the category values to be changed:

```python
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
```

The first three categories are simple enough. First, the password length is checked to see if it is greater than 8 characters. Second, the password is checked for any letters. Third, the password is checked for numbers. However, checking for symbols required the creation of a new function, as Python didn't have any built-in function for this purpose. 

```python
# Special Character checker function
    def special_character_checker(password):
        special_characters = [' ','!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
        '-', '_', '+', '=', '[', ']', '{', '}', ';', ':', ',', '.', '<', '>',
        '/', '?', '\\', '|', '`', '~']
        
        if any(char in special_characters for char in password):
            return True
        else: return False
```

This new function assigns a list of special characters to a variable. Then, the function checks if any of the special characters in the list are found in the password. If they are the function returns "True," and "False" otherwise.

Each of the category variables are assigned "True" or "False" based on their respective checks. 

