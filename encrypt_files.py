
from cryptography.fernet import Fernet
import os

# Generate key and save it
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved to key.key")

# Encrypt a file
def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        data = file.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)
    print(f"{file_path} encrypted successfully.")

# Main
if __name__ == "__main__":
    generate_key()
    key = open("key.key", "rb").read()
    files_to_encrypt = ["main.py", "utils.py"]
    for file in files_to_encrypt:
        if os.path.exists(file):
            encrypt_file(file, key)
