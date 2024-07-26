# Contoh Enkripsi

Repositori ini berisi contoh enkripsi simetris (AES) dan asimetris (RSA) menggunakan Python. Contoh ini menunjukkan bagaimana cara enkripsi dan dekripsi data menggunakan metode enkripsi tersebut.

## Persyaratan

Pastikan Anda telah menginstal pustaka `cryptography`. Anda dapat menginstalnya menggunakan pip:

```bash
pip install cryptography

Enkripsi Simetris (AES)
Script symmetric_encryption.py menunjukkan bagaimana cara enkripsi dan dekripsi data menggunakan AES.

Penggunaan
Enkripsi: Fungsi aes_encrypt mengambil kunci 256-bit dan plaintext sebagai input dan mengembalikan ciphertext.
Dekripsi: Fungsi aes_decrypt mengambil kunci 256-bit dan ciphertext sebagai input dan mengembalikan plaintext.

Contoh
from symmetric_encryption import aes_encrypt, aes_decrypt
import os

key = os.urandom(32)  # Kunci 256-bit
plaintext = "Ini adalah pesan rahasia"

# Enkripsi
ciphertext = aes_encrypt(key, plaintext)
print(f"Encrypted: {ciphertext}")

# Dekripsi
decrypted_text = aes_decrypt(key, ciphertext)
print(f"Decrypted: {decrypted_text}")

Enkripsi Asimetris (RSA)
Script asymmetric_encryption.py menunjukkan bagaimana cara enkripsi dan dekripsi data menggunakan RSA.

Penggunaan
Generate Kunci: Fungsi generate_rsa_keys menghasilkan sepasang kunci RSA (privat dan publik).
Enkripsi: Fungsi rsa_encrypt mengambil kunci publik dan plaintext sebagai input dan mengembalikan ciphertext.
Dekripsi: Fungsi rsa_decrypt mengambil kunci privat dan ciphertext sebagai input dan mengembalikan plaintext.
Contoh

from asymmetric_encryption import generate_rsa_keys, rsa_encrypt, rsa_decrypt

private_key, public_key = generate_rsa_keys()
plaintext = "Ini adalah pesan rahasia"

# Enkripsi
ciphertext = rsa_encrypt(public_key, plaintext)
print(f"Encrypted: {ciphertext}")

# Dekripsi
decrypted_text = rsa_decrypt(private_key, ciphertext)
print(f"Decrypted: {decrypted_text}")

Menjalankan Script
Untuk menjalankan script, gunakan perintah berikut:

python symmetric_encryption.py
python asymmetric_encryption.py

Video Demo

Tonton video demo di sini

Struktur Repositori

EncryptionDemo/
├── asymmetric_encryption.py
├── README.md
└── symmetric_encryption.py

Lisensi
Proyek ini dilisensikan di bawah MIT License - lihat file LICENSE untuk detail.


### Cara Mengunggah ke GitHub

1. **Buat repository baru di GitHub**: Misalnya, beri nama "EncryptionDemo".
2. **Clone repository**:
    ```bash
    git clone https://github.com/username/EncryptionDemo.git
    ```
3. **Pindah ke directory project**:
    ```bash
    cd EncryptionDemo
    ```
4. **Tambahkan file Python dan README.md**:
    ```bash
    touch symmetric_encryption.py asymmetric_encryption.py README.md
    ```
5. **Salin kode di atas ke dalam file yang sesuai**.
6. **Tambahkan file ke repository dan commit**:
    ```bash
    git add .
    git commit -m "Tambah contoh enkripsi simetris dan asimetris"
    git push origin main
    ```

Jika ada pertanyaan lebih lanjut atau bantuan tambahan yang dibutuhkan, beri tahu saya!
