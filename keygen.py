from Crypto.Random import get_random_bytes

with open("key", "wb") as f:
    f.write(get_random_bytes(16))