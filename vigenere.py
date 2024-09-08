def apply_vigenere(message, key, selection):
    result = ""
    key_length = len(key)
    key_index = 0

    for x in message:
        if 'A' <= x <= 'Z':  # Only process uppercase letters
            shift = ord(key[key_index % key_length]) - ord('A')
            if selection == 'DECRYPT':
                # Decrypt by shifting backward
                result += chr((ord(x) - ord('A') - shift) % 26 + ord('A'))
            elif selection == 'ENCRYPT':
                # Encrypt by shifting forward
                result += chr((ord(x) - ord('A') + shift) % 26 + ord('A'))
            key_index += 1
        else:
            result += x  # Preserve non alphabetic characters

    return result


# Input the decryption key
key = input("Input decryption or encryption key:\n").upper()

# Input the ciphertext that you want to decrypt.
ciphertext = input("Input text to encode or decode:\n").upper().replace(" ", "")

selection = input("Would you like to encrypt or decrypt?\n").upper()

# Decrypt the message using the Vigenère cipher.
output = apply_vigenere(ciphertext, key, selection)
print("Output: ", output)

