def encrypt(text,key):
	result=""
	pos=0
	n=len(key)
	for i in range(len(text)):
		result+=  chr ( ( (ord(text[i])-97 + ord(key[pos])-97)%26 )+97)
		pos= (pos+1)%n
	print("Encrypted Text ",result)
		
def decrypt(text,key):
	result=""
	pos=0
	n=len(key)
	for i in range(len(text)):
		result+=  chr ( ( (ord(text[i]) - ord(key[pos]) )%26 )+97)
		pos=(pos+1)%n
	print("Decrypted Text ",result)
		

def main():
	text = input("Enter Text to encrypt/decrypt : ")
	key=input("Enter key : ")
	choice = int(input("Enter 1.Encrypt 2.Decrypt :  "))
	if(1==choice):
		encrypt(text,key)
	else:
		decrypt(text,key)
main()
