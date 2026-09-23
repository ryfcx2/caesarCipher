# Caesar Cipher

### [🔗 GitHub: @ryfcx](https://github.com/ryfcx)

A simple command-line Caesar cipher program written in Python that can encrypt and decrypt words using a user-defined shift value. Made for my CSP2 (Computer Science Principles 2) Highschool course.

## How It Works

The program shifts each letter of a word forward (encryption) or backward (decryption) in the alphabet by a chosen number of positions, wrapping around from `z` back to `a` when needed. Non-letter characters are left unchanged.

## Usage

Run the script, then follow the prompts:

1. Enter a word to encrypt or decrypt.
2. Enter a shift value (how many letters to shift by).
3. Choose `1` to encrypt or `2` to decrypt.

### Example

```
Welcome to the Ceasar Cipher Terminal!
Enter a word: hello
Enter a shift value: 3
Wound you like to encrypt (1) or decrypt (2): 1
Your encrypted word is: khoor
```

## Features

- Encrypts and decrypts lowercase words with any shift value
- Handles wraparound at the end/start of the alphabet
- Basic input validation for menu selection

## Skills Used

- Functions and return values
- Lists and list methods (`.append()`, `.index()`)
- String methods (`.lower()`, `.join()`)
- Conditionals (`if`/`elif`/`else`)
- Loops (`for` loop iteration)
- Exception handling (`try`/`except`)
- User input and type casting

## Author

Made by Ryan for CSP2.
