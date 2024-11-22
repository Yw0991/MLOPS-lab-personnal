# src/validation.py or src/user_functions.py
def get_email_from_input():
    email = input("Tell me your email: ")
    if "@" not in email or "." not in email:
        print('Email is not valid.')
        return None
    return email

def get_user_name_from_input():
    username = input("Create your user name: ")
    if not username or ' ' in username:
        print('Username is not valid.')
        return None
    return username

def get_password_from_input():
    password = input("Create your password: ")
    if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password) or not any(not char.isalnum() for char in password):
        print('Password is not valid.')
        return None
    return password
