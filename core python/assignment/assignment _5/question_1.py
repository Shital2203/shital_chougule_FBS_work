# 1. User Login – Allow 3 attempts


userid = "admin"
password = "1234"
attempts = 0

while attempts < 3:
    uid = input("Enter User ID: ")
    pwd = input("Enter Password: ")
    if uid == userid and pwd == password:
        print("Login Successful ✅")
        break
    else:
        print("Invalid credentials, try again!")
        attempts += 1

if attempts == 3:
    print("Too many attempts! Program terminated.")
    
