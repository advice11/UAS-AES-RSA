from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

def aes_encrypt(key, plaintext):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return iv + ciphertext

def aes_decrypt(key, ciphertext):
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_data = decryptor.update(actual_ciphertext) + decryptor.finalize()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
    return unpadded_data.decode()

key = os.urandom(32)
plaintext = "Ini Pesan Rahasia"
ciphertext = aes_encrypt(key, plaintext)
print(f"Encrypted: {ciphertext}")
decrypted_text = aes_decrypt(key, ciphertext)
print(f"Decrypted: {decrypted_text}")
