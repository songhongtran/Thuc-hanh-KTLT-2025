print("Sinh Vien :TrầnH Võ Sóng Hồng")
print("MSSV:235752020710005")
import re

def check_password(password):
    if (6 <= len(password) <= 12
            and re.search(r"[a-z]", password)
            and re.search(r"[0-9]", password)
            and re.search(r"[A-Z]", password)
            and re.search(r"[$#@]", password)):
        return True
    return False

# Input string of passwords separated by commas
passwords = input("Enter passwords separated by comma: ")

# Split the input string into individual passwords
password_list = passwords.split(',')

# List to store valid passwords
valid_passwords = []
# Check each password
for password in password_list:
    if check_password(password.strip()):
        valid_passwords.append(password.strip())
if valid_passwords:
        print(",".join(valid_passwords))
else:
        print("ko có mật khẩu hợp lệ.")
