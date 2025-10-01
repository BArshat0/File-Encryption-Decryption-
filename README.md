# File Encryptor/Decryptor using Python and Fernet
A simple Python-based tool to **encrypt and decrypt files** using symmetric encryption (Fernet). This project allows you to **secure your sensitive files** locally by converting them into encrypted versions, which can later be decrypted using the same key.
## Features
- Encrypt single or multiple files at once.
- Decrypt encrypted files safely.
- Automatically generates a secret key (`Token.txt`) for encryption and decryption.
- Supports CLI usage for easy automation.
- Handles errors like missing files or invalid keys gracefully.
## How it Works
- Uses the `cryptography` library’s **Fernet** module for strong encryption.
- For each file:
  - **Encryption:** Creates a `.enc` file containing the encrypted data.
  - **Decryption:** Produces a `.dec` file with the original contents.
- Can be run interactively or through command-line arguments using `argparse`.
### Prompts to use in CLI mode
-Navigate to the folder where your script and files are located:
  cd Path to your folder
  
-Use the -e or --encrypt flag followed by one or more filenames:
  python Crypt(CLI).py -e file1.txt file2.txt
  
-Use the -d or --decrypt flag followed by one or more encrypted files:
  python Crypt.py -d file1.txt file2.txt
#### Notes
Keep Token.txt safe; it is required for decryption.

The original files are not overwritten unless you modify the script.

Make sure python(3.8) and cryptography module is installed in your terminal.

