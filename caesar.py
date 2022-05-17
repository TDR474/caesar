# Your code should have two functions: encrypt(key,plaintext) and decrypt(key,ciphertext). 
# They should each take a key and a message. Assume the key is an integer (positive or negative) 
# and the message is a string consisting exclusively of characters from the 26 letters of the alphabet. Assume the string is all in upper case. 
# Your ciphertexts should also consist exclusively of (uppercase) letters (no special characters).


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

# call encrypt and decrypt functions
print(encrypt(3,"HELLO"))
print(decrypt(3,"KHOOR"))
