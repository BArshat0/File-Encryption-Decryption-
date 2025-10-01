import argparse
import os
from cryptography.fernet import Fernet, InvalidToken


#--Generates key and saves it in Token.txt--#
def GenerateKey():
    key = Fernet.generate_key()
    with open("Token.txt", "wb") as token_file:
        token_file.write(key)
#--Reads the key--#
def LoadKey():
    return open("Token.txt", "rb").read()

#--Encrypts the file--#
def Encrypt(filename,key):
    f=Fernet(key)
    with open(filename, "rb") as file:
        data=file.read()
    encrypted_data=f.encrypt(data)
    output_file = filename + ".enc"
    with open(output_file, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    print("The data is encrypted.")


#--Decrypts the file--#
def Decrypt(filename,key):
    f=Fernet(key)
    if not os.path.exists(filename + ".enc"):
        print("Encrypted file not found")
        return
    with open(filename + ".enc","rb") as file:
        data=file.read()
    try:
        decrypted_data=f.decrypt(data)
    except InvalidToken:
        print("Invalid file or wrong key")
        return
    output_file = filename + ".dec"
    with open(output_file, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)
    print("The data is decrypted.")

def main():
    if not os.path.exists("Token.txt"):
        GenerateKey()
    key = LoadKey()
    parser = argparse.ArgumentParser(description= "Encrypt and Decrypt file.")
    parser.add_argument("-e", "--encrypt",nargs="+" , help= "Encrypt file.")

    parser.add_argument("-d", "--decrypt",nargs="+", help= "Decrypt file.")
    args = parser.parse_args()

    if args.encrypt:
        for file in args.encrypt:
            if os.path.exists(file):
                Encrypt(file,key)
            else:
                print("File not found")
    if args.decrypt:
        for file in args.decrypt:
            Decrypt(file,key)

    if not args.encrypt and not args.decrypt:
        parser.print_help()



if __name__ == "__main__":
    main()
