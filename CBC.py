from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

def encrypt_cbc(filename):


    # initialization parameters
    aes_key = get_random_bytes(16)
    offset = 54
    block_size=16


    # Read the file we want to encrypt into memory
    with open(filename, "rb") as f:
        data = bytearray(f.read())   # make editable copy in memory


    # ---- EDITS HERE ----
    iv = get_random_bytes(16)
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)

    # Pad data to be multiple of block size
    padding_byte = block_size - ((len(data)-offset) % block_size)
    for i in range(padding_byte):
        data.append(padding_byte)

    # Encrypt the data in 16-byte blocks
    encrypted_data = data[offset:]
    encrypted_data = bytearray(cipher.encrypt(bytes(encrypted_data)))


    # Write the modified data back to a new file
    with open("output.bmp", "wb") as f:
        f.write(data[:offset])  # Write the header unchanged
        f.write(encrypted_data)  # Write the encrypted data

def encrypt_cbc_text(text):


    # initialization parameters
    aes_key = get_random_bytes(16)
    block_size=16


    # Read the file we want to encrypt into memory
    data = bytearray(text, 'utf-8')   # make editable copy in memory


    # ---- EDITS HERE ----

    # Pad data to be multiple of block size
    padding_byte = block_size - ((len(data)) % block_size)
    for i in range(padding_byte):
        data.append(padding_byte)

    iv = get_random_bytes(16)
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(bytes(data))


    return encrypted_data, aes_key, iv

def decrypt_cbc_text(data, aes_key, iv):


    # ---- EDITS HERE ----
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)

    decrypted_data = cipher.decrypt(data)


    return decrypted_data.decode('utf-8', errors='ignore')
