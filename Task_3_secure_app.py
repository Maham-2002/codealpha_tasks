
import hashlib

# Store only password hash
USERNAME = "admin"

# Hash of password "StrongPassword123!"
STORED_HASH = hashlib.sha256(
    "StrongPassword123!".encode()
).hexdigest()

username = input("Username: ")
password = input("Password: ")

password_hash = hashlib.sha256(
    password.encode()
).hexdigest()

if username == USERNAME and password_hash == STORED_HASH:
    print("Login Successful")
else:
    print("Login Failed")