# Predefined user credentials
correct_username = "admin"
correct_password = "password123"

def authenticate_user():
    # Get user input for username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the entered credentials match the predefined credentials
    if username == correct_username and password == correct_password:
        print("Authentication successful! You have access.")
    else:
        print("Authentication failed. Access denied.")

if __name__ == "__main__":
    authenticate_user()
