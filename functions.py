from random import randint

def encrypt(org_txt):
    
    encrypt = []
    
    rand_num = randint(1,52)
    
    keye = rand_num*56874
    
    keye = hex(keye) 

    for i in org_txt :
        encrypt.append(chr(ord(i)^rand_num))

    en_txt = "".join(encrypt)
    
    return (en_txt ,keye)
    
    
    
    
def decrypt(en_txt ,keyd):
    decrypt=[]
    
    keyd = int(keyd,16)
    
    keyd = int(keyd/56874)
    
    for i in en_txt:
        decrypt.append(chr(ord(i)^keyd))
        
    de_txt = "".join(decrypt)
    
    return de_txt 
  


    
#print(encrypt("shivam"))


#print(decrypt('RIHW@L', '0x1ca36a'))



