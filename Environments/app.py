from User import User

print("Create your account")
user_name = input("Input username : ")
password = input("Input password : ")
new_user = User(user_name, password)
print("Your account created successfully")

print("Login now")
user_name = input("Input username : ")
password = input("Input password : ")
if user_name == new_user.user_name and password == new_user.password:
    print("User Logged in successfully")
else:
    print("Invalid Credential")
