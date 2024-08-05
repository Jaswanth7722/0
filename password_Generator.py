import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def new_password(length=12):
    new_pass = generate_password(length)
    return new_pass
print(f"Generated Password: {new_password()}")
new = "new"
while True :
    print("Type type new for new password :",end=' ')
    user_input = str(input())
    if user_input == new:
        
        print(f"Generated New Password: {new_password()}")