# 8. User login with captcha verification

import random

userid = input("Enter User ID: ")
password = input("Enter Password: ")

if userid == "admin" and password == "1234":
    captcha = random.randint(1000, 9999)
    print("Captcha:", captcha)
    entered = int(input("Enter captcha: "))
    if entered == captcha:
        print("Login Successful ✅")
    else:
        print("Captcha Mismatch ❌")
else:
    print("Invalid User ID or Password")

