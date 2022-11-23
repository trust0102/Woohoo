from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

key = b"academic"
plaintext = b"Hello"

cipher = DES.new(key,DES.MODE_CBC)
ciphertext= cipher.encrypt(pad(plaintext,DES.block_size))
print(ciphertext)

cipher_decrypt = DES.new(key,DES.MODE_CBC,iv=cipher.iv)
print(unpad(cipher_decrypt.decrypt(ciphertext),DES.block_size).decode('utf-8'))
