import random
import string 


# Password generator based of the below variables
    # Must be at least 12 characters long.
    # Must start with a letter.
    # Must contain a digit.
    # Must contain an upper case letter.
    # Must contain a special character.
    # Must not contain the User ID.
    # Must not contain repeating characters(e.g. paSSw0rd,alec11 are invalid).
    # Must not contain the first three letters of any month.
    # Must not have been used within the last 12 months.


def password_generate():
    
    # Variables

    password = ""
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    letters = lowercase + uppercase
    digits = string.digits
    special = string.punctuation
    chars = (letters + digits + special)

    # Parameter variables

    length = 12 # Minimum Length
    haslowercase = False
    hasuppercase = False
    hasdigits = False
    hasspecial = False
    repeatingchars = False
    userID = 5584952 # Redacted
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    previousPW = ['Redacted', 'test']

    # While Loop to add values to password under specific parameters 
  
    while not haslowercase or not hasuppercase or not hasdigits or not hasspecial or len(password) < length:
        char = random.choice(chars)
        password += char

        if char in lowercase:
            haslowercase = True
        elif char in uppercase:
            hasuppercase = True
        elif char in digits:
            hasdigits = True
        elif char in special:
            hasspecial = True
        
    return password

password_generate()