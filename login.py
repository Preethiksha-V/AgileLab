# Login Module

def login(username, password):
    if username == "admin" and password == "admin123":
        print("Login successful")
    else:
        print("Invalid username or password")

def main():
    print("Login Feature")
    username = input("Enter username: ")
    password = input("Enter password: ")
    login(username, password)

if __name__ == "__main__":
    main()
