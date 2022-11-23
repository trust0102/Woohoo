from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

key = get_random_bytes(16)
plaintext = b"Hello"

cipher = DES3.new(key,DES3.MODE_CBC)
ciphertext= cipher.encrypt(pad(plaintext,DES3.block_size))
print(ciphertext)

cipher_decrypt = DES3.new(key,DES3.MODE_CBC,iv=cipher.iv)
print(unpad(cipher_decrypt.decrypt(ciphertext),DES3.block_size).decode('utf-8'))