username = input()
password = input()

while True:
    password_check = input()
    if password_check == password:
        break

print(f"Welcome {username}!")