import argparse
import os
from keygen import generate_key
from Services.Crypter import Crypter

# Создаем аргументы командной строки
parser = argparse.ArgumentParser(description="Encrypting and decrypting file")
parser.add_argument("-action", "-a", type=str, help="Instruction for program. Can be encrypt or decrypt")
parser.add_argument("-input", "-i", type=str, help="Path to input file to encrypt or decrypt")
parser.add_argument("-output", "-o", type=str, help="Path to output file after encryption or decryption")
parser.add_argument("--key", type=str, help="Key for encrypting and decrypting. Can be generated or given right here")
args = parser.parse_args()

# Вывод отладочной информации о переданных аргументах
print(f"Action: {args.action}")
print(f"Input file: {args.input}")
print(f"Output file: {args.output}")
print(f"Key: {args.key}")

# Получаем или генерируем ключ
key = args.key
if not args.key:
    try:
        with open("key", "rb") as f:
            key = f.read()
        print("Key loaded from file 'key'")
    except FileNotFoundError:
        print("Key file not found, generating new key...")
        generate_key()
        with open("key", "rb") as f:
            key = f.read()
        print("New key generated and loaded")

crypter = Crypter(key)

if args.action == "encrypt":
    # Проверка на существование входного файла
    if not os.path.isfile(args.input):
        print(f"Error: Input file {args.input} does not exist.")
    else:
        try:
            print(f"Encrypting file {args.input}...")
            crypter.encrypt(args.input, args.output)
            print(f"File encrypted and saved as {args.output}")
        except FileNotFoundError as ex:
            print(f"Error during encryption: {ex}")
elif args.action == "decrypt":
    # Проверка на существование входного файла
    if not os.path.isfile(args.input):
        print(f"Error: Input file {args.input} does not exist.")
    else:
        try:
            print(f"Decrypting file {args.input}...")
            crypter.decrypt(args.input, args.output)
            print(f"File decrypted and saved as {args.output}")
        except ValueError:
            print("Wrong key for decryption!")
        except Exception as ex:
            print(f"Error during decryption: {ex}")
else:
    print(f"Invalid action: {args.action}. Please specify 'encrypt' or 'decrypt'.")
