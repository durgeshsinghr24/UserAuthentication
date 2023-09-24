# Predefined user credentials for different authentication methods
correct_username = "admin"
correct_password = "password123"
secret_passcode = "123456"

correct_password_2 = "password123"
correct_security_code = "9876"
correct_name = "John"

import random
import string

# Function to generate a random 5-letter CAPTCHA
def generate_captcha():
    captcha = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    return captcha

# Dummy user data for CAPTCHA authentication
user_database = [
    {'username': 'admin1', 'password': 'password1'},
    {'username': 'admin2', 'password': 'password2'},
    {'username': 'admin3', 'password': 'password3'},
]

# Function to authenticate the user with CAPTCHA
def authenticate_captcha(username, password, entered_captcha):
    for user in user_database:
        if user['username'] == username and user['password'] == password:
            # Generate a random CAPTCHA
            captcha = generate_captcha()
            print(f'Generated CAPTCHA: {captcha}')
            
            # Verify CAPTCHA and authenticate the user
            if entered_captcha == captcha:
                return True
    return False

# Function to handle username/password authentication
def authenticate_username_password(username, password):
    return username == correct_username and password == correct_password

# Function to handle username/password/secret passcode authentication
def authenticate_username_password_passcode(username, password, entered_passcode):
    if username == correct_username and password == correct_password:
        if entered_passcode == secret_passcode:
            return True
    return False

# Function to handle name/password/security code authentication
def authenticate_name_password_security(name, password, security_code):
    return name == correct_name and password == correct_password_2 and security_code == correct_security_code

if __name__ == '__main__':
    print("Choose the type of authentication:")
    print("1. Simple Password Authentication")
    print("2. Two-factor Authentication")
    print("3. CAPTCHA Authentication")
    print("4. Multi-factor Authentication")
    
    choice = input("Enter the number of your choice: ")
    
    if choice == '1':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if authenticate_username_password(username, password):
            print("Authentication successful!")
        else:
            print("Authentication failed. Access denied.")
    
    elif choice == '2':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        entered_passcode = input("Enter the secret passcode: ")
        if authenticate_username_password_passcode(username, password, entered_passcode):
            print("Authentication successful!")
        else:
            print("Authentication failed. Access denied.")
    
    elif choice == '3':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        entered_captcha = input(f'Enter the CAPTCHA ({generate_captcha()}): ')
        if authenticate_captcha(username, password, entered_captcha):
            print("Authentication successful!")
        else:
            print("Authentication failed. Access denied.")
    
    elif choice == '4':
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        security_code = input("Enter the security code: ")
        if authenticate_name_password_security(name, password, security_code):
            print("Authentication successful!")
        else:
            print("Authentication failed. Access denied.")
    
    else:
        print("Invalid choice. Please select a valid authentication method.")
