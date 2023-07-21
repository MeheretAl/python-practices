import string
import secrets
special_characters = "~`!@#$%^&*()-_+=|}{:<>?\'\"" 
chars = string.ascii_uppercase + string.digits + string.ascii_lowercase + special_characters

print("".join(secrets.choice(chars) for i in range(8)))