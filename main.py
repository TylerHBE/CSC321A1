import ECB
import CBC2 as CBC
import bitflip

# Task 1
# encrypting the cp-logo image using both ECB and CBC modes

ECB.encrypt_ecb("cp-logo.bmp")
CBC.encrypt_cbc("cp-logo.bmp")

# Task 2
# demonstrating the bit-flip attack on CBC mode
bitflip.bit_flip_attack()