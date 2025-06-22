from cryptography.fernet import Fernet
import os


class Encrypt_Decrypt:
    def __init__(self, username, password):
        self.User = username
        self.password = password

    def encrypt_pass(self):
        key = Fernet.generate_key()
        keyfilename = f"{self.User}.key"
        
        with open(keyfilename, "wb") as key_file:
            key_file.write(key)

        with open(keyfilename, "rb") as key_file:
            key = key_file.read()

        fernet = Fernet(key)
        encrypted_password = fernet.encrypt(self.password.encode())

        curr_dir = os.getcwd()
        user_dir = os.path.join(curr_dir, "Users")
        os.makedirs(user_dir, exist_ok=True)

        filepath = os.path.join(user_dir, f"{self.User}_encrypted.txt")
        with open(filepath, "wb") as enc_file:
            enc_file.write(encrypted_password)

        print(f"Key saved as: {keyfilename}")
        print(f"Encrypted password saved at: {filepath}")

    def decrypt_pass(self):
    
        keyfilename = f"{self.User}.key"
        key_path = os.path.join(os.getcwd(), keyfilename)

        if not os.path.exists(key_path):
            print("Key file not found!")
            return

        with open(key_path, "rb") as key_file:
            key = key_file.read()

        fernet = Fernet(key)

        encrypted_file = os.path.join(os.getcwd(), "Users", f"{self.User}_encrypted.txt")
        if not os.path.exists(encrypted_file):
            print("Encrypted password file not found!")
            return

        with open(encrypted_file, "rb") as enc_file:
            encrypted_password = enc_file.read()

        try:
            decrypted_password = fernet.decrypt(encrypted_password).decode()
            print(f"Decrypted password for user '{self.User}': {decrypted_password}")
        except Exception as e:
            print("Decryption failed:", e)

# Example usage
x1 = Encrypt_Decrypt(str(input("Enter Username: ")), str(input("Enter Password: ")))
x1.encrypt_pass()