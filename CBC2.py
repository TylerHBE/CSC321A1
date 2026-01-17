from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_cbc(filename: str):
    block_size = 16
    offset = 54 

    # Cipher parameters
    aes_key = get_random_bytes(16)
    iv = get_random_bytes(block_size)
    cipher = AES.new(aes_key, AES.MODE_ECB)

    # Read file into memory
    with open(filename, "rb") as f:
        data = bytearray(f.read())

    plaintext = data[offset:]

    # Padding
    pad_len = block_size - (len(plaintext) % block_size)
    plaintext += bytes([pad_len] * pad_len)

    encrypted_data = bytearray()
    prev_block = iv
    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i+block_size]
        block = bytes([b ^ p for b, p in zip(block, prev_block)])
        encrypted_block = cipher.encrypt(block)
        encrypted_data.extend(encrypted_block)
        prev_block = encrypted_block

    # Write encrypted image to file
    with open("output_CBC.bmp", "wb") as f:
        f.write(data[:offset])
        f.write(encrypted_data)

def encrypt_cbc_text(text: str):
    block_size = 16

    # Cipher parameters
    aes_key = get_random_bytes(16)
    iv = get_random_bytes(block_size)
    cipher = AES.new(aes_key, AES.MODE_ECB)

    # Read file into memory
    
    plaintext = bytearray(text, 'utf-8')

    # Padding
    pad_len = block_size - (len(plaintext) % block_size)
    plaintext += bytes([pad_len] * pad_len)

    encrypted_data = bytearray()
    prev_block = iv
    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i+block_size]
        block = bytes([b ^ p for b, p in zip(block, prev_block)])
        encrypted_block = cipher.encrypt(block)
        encrypted_data.extend(encrypted_block)
        prev_block = encrypted_block

    # return encrypted data
    return encrypted_data, aes_key, iv

def decrypt_cbc_text(data, aes_key, iv):

    cipher = AES.new(aes_key, AES.MODE_CBC, iv)

    decrypted_data = cipher.decrypt(data)

    return decrypted_data.decode('utf-8', errors='ignore')