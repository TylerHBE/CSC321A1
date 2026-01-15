from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import urllib.parse
import CBC


def submit(message):
    tmpstring = "serid=456;userdata=" + message
    tmpstring += ";session-id=31337"
    urlstring = tmpstring.replace(";", "43B").replace("=", "%3D")
    encrypted_text, key, iv = CBC.encrypt_cbc_text(urlstring)
    return encrypted_text, key, iv

def verify(message, key, iv) -> bool:
    unencrypted_text = CBC.decrypt_cbc_text(message, key, iv)
    print(unencrypted_text)
    if unencrypted_text.find(";admin=true") != -1:
        return True
    return False


if __name__ == "__main__":
    message = ";admin=true"
    text, key, iv = submit(message)
    #edit the text
    text = bytearray(text)
    #for some reason everything gets scrambled if I try and cross over from one block into another
    #should be proper bit flips with my understanding
    #take the index of which character you want to swap
    #subtract 16-1 (basically)
    # xor by (character_there ^ character_you_want)
    # text[11] = text[11] ^ 0x79
    # text[17] = text[17] ^ 0x18
    # text[18] = text[18] ^ 0x47
    # text[19] = text[19] ^ 0x36
    # text[20] = text[20] ^ 0x1
    # text[21] = text[21] ^ 0x17
    # text[11] = text[11] ^ 0x79

    #worse solution because I struggled with debugging, I am only working in one block of 16 bytes
    #%->;
    text[17] = text[17] ^ 0x1e
    #3->a
    text[18] = text[18] ^ 0x52
    #D->d
    text[19] = text[19] ^ 0x20
    #t->m
    text[20] = text[20] ^ 0x19
    #r->i
    text[21] = text[21] ^ 0x1b
    #u->n
    text[22] = text[22] ^ 0x1b
    #e->=
    text[23] = text[23] ^ 0x58
    #4->t
    text[24] = text[24] ^ 0x40
    #3->r
    text[25] = text[25] ^ 0x41
    #B->u
    text[26] = text[26] ^ 0x37
    #s->e
    text[27] = text[27] ^ 0x16

    print(verify(text, key, iv))

