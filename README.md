# Vigen-re-Cipher-Encoder-Decoder
This project provides a Python-based implementation of the Vigenère Cipher for encoding and decoding text using a keyword. The cipher applies a sequence of shifts to each letter in the message based on the letters of the key. This tool allows you to both encrypt and decrypt text using the same logic.
How It Works

    Key: The user inputs a keyword that is repeated to match the length of the message.
    Message: The user provides the text they want to encrypt or decrypt.
    Selection: The user chooses whether to perform encryption or decryption.
    Output: The processed message (encrypted or decrypted) is displayed as output.

Features

    Supports both encryption and decryption modes.
    Handles uppercase alphabetic characters.
    Non-alphabetic characters (e.g., spaces, punctuation) are preserved and unaffected by the cipher.
    Works with any length of message and key.

Usage

    Run the script in a Python 3.x environment.
    Input the encryption/decryption key (case insensitive).
    Input the message (plaintext or ciphertext) to process.
    Select either ENCRYPT or DECRYPT to specify the operation.

Example

bash
    
    Input decryption or encryption key:
    SECRET
    
    Input text to encode or decode:
    HELLO WORLD
    
    Would you like to encrypt or decrypt?
    ENCRYPT
    
    Output: ZIGGNKGLRM

In this example, the message HELLO WORLD was encrypted using the key SECRET.
Example 2: Decryption

bash
    
    Input decryption or encryption key:
    SECRET
    
    Input text to encode or decode:
    ZIGGNKGLRM
    
    Would you like to encrypt or decrypt?
    DECRYPT
    
    Output: HELLOWORLD

Requirements

    Python 3.x

Running the Script

To run the program, open a terminal and execute the following command:

bash

    python vigenere.py
