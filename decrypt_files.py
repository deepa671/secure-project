
from cryptography.fernet import Fernet

# Decrypt a file
def decrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)
    print(f"{file_path} decrypted successfully.")

# Main
if __name__ == "__main__":
    key = input("Enter the decryption key: ").encode()
    files_to_decrypt = ["main.py", "utils.py"]
    for file in files_to_decrypt:
        decrypt_file(file, key)
