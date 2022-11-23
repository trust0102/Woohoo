from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

key = get_random_bytes(16) 
plaintext = b"Cryptography"

cipher = AES.new(key,AES.MODE_CBC)
ciphertext= cipher.encrypt(pad(plaintext,AES.block_size))
print(ciphertext)

cipher_decrypt = AES.new(key,AES.MODE_CBC,iv=cipher.iv)
print(unpad(cipher_decrypt.decrypt(ciphertext),AES.block_size).decode('utf-8'))
