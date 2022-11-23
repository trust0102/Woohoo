def encrypt(text,depth):
    n=len(text)
    row=depth
    text+= 'x'*( (-(n%row))%row)
    col= (n//row)
    cmat = [['' for j in range(col)]for i in range(row)]
    k=0
    for i in range(col):
        for j in range(row):
            cmat[j][i]=text[k]
            k+=1

    ctext=""
    for i in range(row):
        for j in range(col):
            ctext+=cmat[i][j]
    print("Encrypted Text ",ctext)

def decrypt(text,depth):
    n=len(text)
    row=depth
    col= (n//row)

    cmat = [['' for j in range(col)]for i in range(row)]
    k=0
    for i in range(row):
        for j in range(col):
            cmat[i][j]=text[k]
            k+=1

    ptext=""
    for i in range(col):
        for j in range(row):
            ptext+=cmat[j][i]
    print("Decrypted Text ",ptext)

def main():
    text = input("Enter Text to encrypt/decrypt : ")
    depth=int(input("Enter key : ")) #depth can be inferred as key
    choice = int(input("Enter 1.Encrypt 2.Decrypt : "))
    if(1==choice):
        encrypt(text,depth)
    else:
        decrypt(text,depth)

main()