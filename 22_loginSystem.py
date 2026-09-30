username = input("Enter your username: ")
password = input("Enter your password: ")
print(f"username: {username}")
print(f"password: {password}")

if username == "admin" and password == "1234":
    print("Login successful!")
else:
    print("Login failed. Please check your username and password.")