# Enkripsi Symetric Encryption (AES) dan Asymetric Encryption (RSA)

Repositori ini berisi contoh enkripsi simetris (AES) dan asimetris (RSA) menggunakan Python. Contoh ini menunjukkan bagaimana cara enkripsi dan dekripsi data menggunakan metode enkripsi tersebut.

## Symetric Encryption (AES)
Script aes.py menunjukkan bagaimana cara enkripsi dan dekripsi data menggunakan AES.

### Penggunaan
- Enkripsi : Fungsi aes_encrypt mengambil kunci 256-bit dan plaintext sebagai input dan mengembalikan ciphertext.
- Dekripsi : Fungsi aes_decrypt mengambil kunci 256-bit dan ciphertext sebagai input dan mengembalikan plaintext.

### Contoh : 

```python
from symmetric_encryption import aes_encrypt, aes_decrypt
import os

key = os.urandom(32)  # Kunci 256-bit
plaintext = "Ini adalah pesan rahasia"
```

- Enkripsi
```python
ciphertext = aes_encrypt(key, plaintext)
print(f"Encrypted: {ciphertext}")
```

- Dekripsi
```python
decrypted_text = aes_decrypt(key, ciphertext)
print(f"Decrypted: {decrypted_text}")
```

## Enkripsi Asimetris (RSA)
Script rsa.py menunjukkan bagaimana cara enkripsi dan dekripsi data menggunakan RSA.

### Penggunaan
- Generate Kunci: Fungsi generate_rsa_keys menghasilkan sepasang kunci RSA (privat dan publik).
- Enkripsi: Fungsi rsa_encrypt mengambil kunci publik dan plaintext sebagai input dan mengembalikan ciphertext.
- Dekripsi: Fungsi rsa_decrypt mengambil kunci privat dan ciphertext sebagai input dan mengembalikan plaintext.

### Contoh : 

```python
from asymmetric_encryption import generate_rsa_keys, rsa_encrypt, rsa_decrypt

private_key, public_key = generate_rsa_keys()
plaintext = "Ini adalah pesan rahasia"
```

- Enkripsi
```python
ciphertext = rsa_encrypt(public_key, plaintext)
print(f"Encrypted: {ciphertext}")
```

- Dekripsi
```python
decrypted_text = rsa_decrypt(private_key, ciphertext)
print(f"Decrypted: {decrypted_text}")
```

## Persyaratan
Pastikan Anda telah menginstal pustaka `cryptography`. Anda dapat menginstalnya menggunakan pip:

```bash
pip install cryptography
```

lakukan upgrade versi bila ada versi baru

## Menjalankan Script
Untuk menjalankan script, gunakan perintah berikut:

```bash
python aes.py
python rsa.py
```

## Video Demo

Tonton video demo di sini [ini](https://drive.google.com/file/d/1tAvDqy-VowmOCFNm_CjSNHOGkrwgIx6G/view?usp=sharing)

## Struktur Repositori

```bash
UAS-AES-RSA/
├── aes.py
├── README.md
└── rsa.py
```

## Cara Mengunggah ke GitHub

1. **Buat repository baru di GitHub**: Misalnya, beri nama "UAS-AES-RSA".
2. **Clone repository**:
    ```bash
    git clone https://github.com/advice11/UAS-AES-RSA.git
    ```
3. **Pindah ke directory project**:
    ```bash
    cd UAS-AES-RSA
    ```
4. **Tambahkan file Python dan README.md**:
    ```bash
    touch aes.py rsa.py README.md
    ```
5. **Salin kode di atas ke dalam file yang sesuai**.
6. **Tambahkan file ke repository dan commit**:
    ```bash
    git add .
    git commit -m "Tambah contoh enkripsi simetris dan asimetris"
    git push origin main
    ```
