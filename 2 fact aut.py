# Predefined user credentials
correct_username = "admin"
correct_password = "password123"
secret_passcode = "123456"  # The secret passcode

def authenticate_user():
    # Get user input for username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the entered credentials match the predefined credentials
    if username == correct_username and password == correct_password:
        print("Authentication successful! Please enter the secret passcode.")
        
        # Get user input for the secret passcode
        entered_passcode = input("Enter the secret passcode: ")
        
        # Check if the entered passcode matches the predefined passcode
        if entered_passcode == secret_passcode:
            print("2FA successful! You have access.")
        else:
            print("2FA failed. Access denied.")
    else:
        print("Authentication failed. Access denied.")

if __name__ == "__main__":
    authenticate_user()
