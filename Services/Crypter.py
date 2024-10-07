from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class Crypter:
    def __init__(self, key):
        """Initializing key, mode, block size and en/decrypter"""
        try:
            self.key = self.__generate_key(key)
        except Exception as ex:
            self.key = key
        self.mode = AES.MODE_ECB
        self.BLOCK_SIZE = 16
        self.crypter = AES.new(self.key, self.mode)

    def __generate_key(self, key):
        """Makes 16 byte key from string"""
        if len(key) < 16: key += "0" * (16 - len(key))
        else: key = key[:16]
        return key.encode("utf-8")
    
    def get_key(self):
        return self.key

    def encrypt(self, path_to_input, path_to_output):
        """Encrypts data"""
        res = ""
        with open(path_to_input, "rb") as f:
            data = f.read()
            res = self.crypter.encrypt(pad(data, self.BLOCK_SIZE))
        with open(path_to_output, "wb") as f:
            f.write(res)
            
    
    def decrypt(self, path_to_input, path_to_output):
        """Decrypts data"""
        res = ""
        with open(path_to_input, "rb") as f:
            data = f.read()
            res = unpad(self.crypter.decrypt(data), self.BLOCK_SIZE)
        with open(path_to_output, "wb") as f:
            f.write(res)