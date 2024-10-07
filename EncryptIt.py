import argparse
import os
from Services.Crypter import Crypter

parser = argparse.ArgumentParser(description="Ecnrypting and decrypting file")
parser.add_argument("-action", "-a", type=str, help="Instruction for program. Can be encypt or decrypt")
parser.add_argument("-input", "-i", type=str, help="Path to input file to encrypt")
parser.add_argument("-output", "-o", type=str, help="Path to input file to encrypt")
parser.add_argument("--key", type=str, help="Key for encrypting and decrypting. Can be generated or given right here")
args = parser.parse_args()

key = args.key
if not(args.key):
    with open("key", "rb") as f:
        key = f.read()

crypter = Crypter(key)
if args.action == "encrypt":
    try:
        crypter.encrypt(args.input, args.output)
    except FileNotFoundError as ex:
        print("Invalid file location!")
elif args.action == "decrypt":
    try:
        crypter.decrypt(args.input, args.output)
    except FileNotFoundError:
        print("Invalid file location!")
else:
    print("Invalid action!")    
