from Crypto.Random import get_random_bytes

def generate_key():
    with open("key", "wb") as f:
        f.write(get_random_bytes(16))

if __name__ == "__main__":
    generate_key()