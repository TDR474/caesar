
def encrypt(key,plaintext):
    ciphertext=""
    # shift plaintext key places to the right to become cipher text
    # Cesar's cipher with shift parameter of key
    for i in range(len(plaintext)):
        ciphertext += chr(ord(plaintext[i]) + key)
    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    for i in range(len(ciphertext)):
        plaintext += chr(ord(ciphertext[i]) - key)
    return plaintext
