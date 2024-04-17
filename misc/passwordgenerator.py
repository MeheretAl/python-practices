import string
import secrets

special_characters = "~`!@#$%^&*()-_+=|}{:<>?\'\"" 
chars = string.ascii_uppercase + string.digits + string.ascii_lowercase + special_characters

def random_password_generator(length=5):
    generatedpassword = "".join(secrets.choice(chars) for i in range(length))
    return generatedpassword

