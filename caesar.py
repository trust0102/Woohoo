def encrypt(text,key):
	result=""
	for i in range(len(text)):
		result+=   chr( ( (ord(text[i])-97+key)%26 )+97)
	print("Encrypted Text ",result)
	
def decrypt(text,key):
	result=""
	for i in range(len(text)):
		result+=   chr( ( (ord(text[i])-97-key)%26 )+97)
	print("Decrypted Text ",result)

def main():
	text = input("Enter Text to encrypt/decrypt : ")
	key=int(input("Enter key : "))
	choice = int(input("Enter 1.Encrypt 2.Decrypt :  "))
	if(1==choice):
		encrypt(text,key)
	else:
		decrypt(text,key)
main()
