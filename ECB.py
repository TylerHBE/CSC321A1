from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_ecb(filename):


    # initialization parameters
    aes_key = get_random_bytes(16)
    offset = 54
    block_size=16


    # Read the file we want to encrypt into memory
    with open(filename, "rb") as f:
        data = bytearray(f.read())   # make editable copy in memory


    # ---- EDITS HERE ----
    cipher = AES.new(aes_key, AES.MODE_ECB)

    # Pad data to be multiple of block size
    padding_byte = block_size - ((len(data)-offset) % block_size)
    for i in range(padding_byte):
        data.append(padding_byte)

    # Encrypt the data in 16-byte blocks
    encrypted_data = bytearray()
    for i in range(offset, len(data), block_size):
        block = data[i:i+block_size]
        # Pad block if it's less than 16 bytes, although this should not happen due to previous padding
        if len(block) < block_size:
            block.extend([0] * (block_size - len(block)))
        encrypted_block = cipher.encrypt(bytes(block))
        encrypted_data.extend(encrypted_block)

    # Write the modified data back to a new file
    with open("output_ECB.bmp", "wb") as f:
        f.write(data[:offset])  # Write the header unchanged
        f.write(encrypted_data)  # Write the encrypted data