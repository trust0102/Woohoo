def encrypt(text,key):
    n=len(text)
    col=len(key)
    text+= 'x'*( (-(n%col))%col)
    n=len(text)
    row= (n//col)
    cmat = [['' for j in range(col)]for i in range(row)]
    k=0
    for i in range(row):
        for j in range(col):
            cmat[i][j]=text[k]
            k+=1
            
    sort_key=sorted(list(key))
    ctext=""
    for i in range(col):
        curr_col = key.find(sort_key[i])
        ctext+= ''.join([cmat[i][curr_col] for i in range(row)])
    print("Encrypted Text ",ctext)

def decrypt(text,key):
    n=len(text)
    col=len(key)
    row= (n//col)

    cmat = [['' for j in range(col)]for i in range(row)]
    k=0
    sort_key=sorted(list(key))
    for i in range(col):
        curr_col= key.find(sort_key[i])
        for j in range(row):
            cmat[j][curr_col]=text[k]
            k+=1

    ptext=""
    for i in range(row):
        for j in range(col):
            ptext+=cmat[i][j]
    print("Decrypted Text ",ptext)

def main():
    text = input("Enter Text to encrypt/decrypt : ")
    key = input("Enter the key : ")
    choice = int(input("Enter 1.Encrypt 2.Decrypt : "))
    if(1==choice):
        encrypt(text,key)
    else:
        decrypt(text,key)

main()