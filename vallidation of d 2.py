def encrypt(message, e, n):
    # Encrypt the message and convert each encrypted integer to a string
    ciphertext = [pow(ord(char), e, n) for char in message]
    # Convert the list of integers to a string with a custom separator
    return ' '.join(map(str, ciphertext))

def decrypt(ciphertext, d, n):
    # Split the ciphertext string back into a list of integers
    ciphertext_list = list(map(int, ciphertext.split()))
    # Decrypt each integer and convert it back to the corresponding character
    return ''.join([chr(pow(char, d, n)) for char in ciphertext_list])

e = int(input("Enter the public key exponent (e): "))
n = int(input("Enter the modulus (n): "))
d = int(input("Enter the private key exponent (d): "))

message = input("Enter the message to encrypt: ")

# Encrypt the message
ciphertext = encrypt(message, e, n)
print("Encrypted message:", ciphertext)

# Decrypt the message
decrypted_message = decrypt(ciphertext, d, n)
print("Decrypted message:", decrypted_message)
