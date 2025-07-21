def pw_inspector(password):
    issuses = []
    if not password:
        issuses.append("Please enter a password")    
    if len(password) < 8:
        issuses.append("at least 8 characters")    
    if not any(char.isdigit() for char in password):
        issuses.append("contain at least one digit")
    if not any(char.isupper() for char in password):
        issuses.append("contain at least one uppercase letter")
    if not any(char.islower() for char in password):
        issuses.append("contain at least one lowercase letter")
    if not any(char in "!@#$%^&*()-_=+[]{}|;:',.<>?/" for char in password):
        issuses.append("contain at least one special character")
    if issuses:
        return ", ".join(issuses)
    return "great password"
if __name__ == "__main__":
    while True:
        input_password = input("Please enter a password: ")
        result = pw_inspector(input_password)
        print(result)