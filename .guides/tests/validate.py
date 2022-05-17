#!/usr/bin/env python3
import random

def validate():
    try:
        import caesar
    except ImportError:
        print("Could not import homework file 'caesar.py'")
        raise ImportError("Could not import homework file 'caesar.py'")

    required_methods = ["encrypt","decrypt"]
    for m in required_methods:
        if m not in dir(caesar):
            print( "%s not defined"%m )
            return 0

    num_tests = 5
    num_passed = 0
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(num_tests):
            print("=========== Running test %d ==========="%(i+1))
            key = random.SystemRandom().randint(0,25)
            plaintext = "".join( [random.SystemRandom().choice(LETTERS) for _ in range(32)] )
            try:
                ciphertext = caesar.encrypt(key,plaintext)
            except Exception as e:
                print( "ERROR: encrypt failed" )
                continue
            print( "encrypt ran without errors" )
            try:
                decryption = caesar.decrypt(key,ciphertext)
            except Exception as e:
                print( "ERROR: decrypt failed" )
                continue
            print( "decrypt ran without errors" )
            if plaintext == decryption:
                print( "Decryption seems to invert encryption" )
                num_passed = num_passed + 1
            else:
                print( "ERROR: Decryption failed" )

    return 2 * num_passed * 10


