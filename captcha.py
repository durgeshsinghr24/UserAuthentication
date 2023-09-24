import random
import string

# Function to generate a random 5-letter CAPTCHA
def generate_captcha():
    captcha = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    return captcha

# Dummy user data (replace with your authentication logic)
user_database = [
    {'username': 'user1', 'password': 'pass1'},
    {'username': 'user2', 'password': 'pass2'},
    {'username': 'user3', 'password': 'pass3'},
]

# Function to authenticate the user
def authenticate(username, password):
    for user in user_database:
        if user['username'] == username and user['password'] == password:
            return True
    return False

# Main program
if __name__ == '__main__':
    # Generate a random CAPTCHA
    captcha = generate_captcha()
    
    # Prompt the user for input
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    entered_captcha = input(f'Enter the CAPTCHA ({captcha}): ')
    
    # Verify CAPTCHA and authenticate the user
    if entered_captcha == captcha:
        if authenticate(username, password):
            print('Authentication successful!')
        else:
            print('Invalid username or password.')
    else:
        print('CAPTCHA verification failed.')
