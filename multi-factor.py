# Predefined user credentials
correct_password = "password123"
correct_security_code = "9876"
correct_name = "John Doe"

def authenticate_user():
    # Get user input for name, password, and security code
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    security_code = input("Enter the security code: ")

    # Check if the entered credentials match the predefined credentials
    if name == correct_name and password == correct_password and security_code == correct_security_code:
        print("MFA successful! You have access.")
    else:
        print("MFA failed. Access denied.")

if __name__ == "__main__":
    authenticate_user()
