from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def generate_rsa_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

def rsa_encrypt(public_key, plaintext):
    ciphertext = public_key.encrypt(
        plaintext.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

def rsa_decrypt(private_key, ciphertext):
    decrypted_data = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_data.decode()

private_key, public_key = generate_rsa_keys()
plaintext = "Ini Pesan Rahasia"
ciphertext = rsa_encrypt(public_key, plaintext)
print(f"Encrypted: {ciphertext}")
decrypted_text = rsa_decrypt(private_key, ciphertext)
print(f"Decrypted: {decrypted_text}")
