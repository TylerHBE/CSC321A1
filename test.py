import CBC
import ECB
import bitflip

encoded_text, aes_key, iv = CBC.encrypt_cbc_text("cp-logo.bmp")

print("Encrypted text (CBC):", encoded_text)

decoded_text = CBC.decrypt_cbc_text(encoded_text, aes_key, iv)

print("Decrypted text (CBC):", decoded_text)

CBC.encrypt_cbc("cp-logo.bmp")

bitflip.bit_flip_attack()
