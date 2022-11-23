class TwoWayDict(dict):
    def __len__(self):
       return dict.__len__(self) / 2

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        dict.__setitem__(self, value, key)

d = TwoWayDict()

def fill_key_matrix(key):
	count=0
	for i in key:
		if(i not in d.keys()):
			d[i]=count
			count+=1
	for i in range(97,123,1):
		if(chr(i) not in d.keys() and chr(i)!='j'):
			d[chr(i)]=count
			count+=1
	


def normalize(text):
	result=text[0]
	for i in range(1,len(text)):
		if(text[i]==text[i-1]):
			result+="x"+text[i]
		else:
			result+=text[i]
	if(len(result)%2!=0):
		result+="x"
	return result

def encrypt(text,key):
	text = normalize(text)
	result=""
	for i in range(0,len(text),2):
		row1 = d[text[i]]//5 #integer division
		col1 = d[text[i]]%5
		row2 = d[text[i+1]]//5
		col2 = d[text[i+1]]%5
		if(row1==row2):
			col1=(col1+1)%5
			col2=(col2+1)%5
			result+=d[row1*5+col1]
			result+=d[row2*5+col2]
		elif(col1==col2):
			row1=(row1+1)%5
			row2=(row2+1)%5
			result+=d[row1*5+col1]
			result+=d[row2*5+col2]
		else:
			result+=d[row1*5+col2]
			result+=d[row2*5+col1]
	print("Encrypted Text : ", result)

def decrypt(text,key):	
	result=""
	for i in range(0,len(text),2):
		row1 = d[text[i]]//5 #integer division
		col1 = d[text[i]]%5
		row2 = d[text[i+1]]//5
		col2 = d[text[i+1]]%5
		if(row1==row2):
			col1=(col1-1)%5
			col2=(col2-1)%5
			result+=d[row1*5+col1]
			result+=d[row2*5+col2]
		elif(col1==col2):
			row1=(row1-1)%5
			row2=(row2-1)%5
			result+=d[row1*5+col1]
			result+=d[row2*5+col2]
		else:
			result+=d[row1*5+col2]
			result+=d[row2*5+col1]

	print("Decrypted Text : ",result)


def main():
	text = input("Enter Text to encrypt/decrypt : ")
	text=text.replace("j","i")
	key= input("Enter key : ")
	key.replace("j","i")
	fill_key_matrix(key)
	
	choice = int(input("Enter 1.Encrypt 2.Decrypt :  "))
	if(1==choice):
		encrypt(text,key)
	else:
		decrypt(text,key)

main()
