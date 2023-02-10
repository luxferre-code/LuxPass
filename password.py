import base64
import hashlib
import os
from Crypto.Cipher import AES
import random

def encrypt_password(password_to_encrypt: str, master_key: str) -> str:
    """Encrypt password"""
    key = hashlib.sha256(master_key.encode()).digest()
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return base64.b64encode(iv + cipher.encrypt(password_to_encrypt.encode())).decode()


def decrypt_password(password_to_decrypt: str, master_key: str) -> str:
    """Decrypt password"""
    key = hashlib.sha256(master_key.encode()).digest()
    password_to_decrypt = base64.b64decode(password_to_decrypt)
    iv = password_to_decrypt[:16]
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return cipher.decrypt(password_to_decrypt[16:]).decode()


def hash_password(password_to_hash: str) -> str:
    """Hash password"""
    return hashlib.sha256(password_to_hash.encode()).hexdigest()

def generate_password(taille: int) -> str:
    """Generate password"""
    return ''.join([chr(random.randint(33, 126)) for _ in range(taille)])

if __name__ == "__main__":
    hashed = hash_password("password")
    encrypt = encrypt_password("password", hashed)
    print(encrypt)
    print(decrypt_password(encrypt, hashed))
    print(hashed)