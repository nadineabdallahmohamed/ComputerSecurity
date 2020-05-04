
from struct import pack, unpack

strg = '{}'

def F(w):
    return ((w * 31337) ^ (w * 1337 >> 16)) % 2**32
''' 
   Return the original text after decrypting it
'''

def decrypt_ciphers(block_cipher):    
    int1, int2, int3, int4 = unpack('<4I', block_cipher)    
    for idx in range(32):       
        tmp = int1
        int4 = int4 ^ 1337
        int1 = int3 ^ (F(int4 | F(int4) ^ int4))
        int2 = int2 ^ (F(int4 ^ F(int1) ^ (int4 | int1)))
        int3 = tmp ^ (F(int4 | F(int2 ^ F(int1)) ^ F(int4 | int2) ^ int1))     
        tmp = int1
        int1 = int4 ^ 31337
        int4 = int3 ^ (F(int1 | F(int1) ^ int1))
        int3 = int2 ^ (F(int1 ^ F(int4) ^ (int1 | int4)))
        int2 = tmp ^ (F(int1 | F(int3 ^ F(int4)) ^ F(int1 | int3) ^ int4))    
    bytes = pack('<4I', int1, int2, int3, int4)
    return bytes 
      
''' 
    Open the "flag.enc" file in binary format "rb" mode for reading 
    iterate over every 16 bytes of the ciphertext and print out the original text
 '''
encrypted_text = open('flag.enc','rb').read()

def edit_text(txt):
    new_str = strg.format(txt)[2:-1]
    return new_str
    

decrypted_text = "".join(edit_text(decrypt_ciphers(encrypted_text[idx:idx+16])) for idx in range(0,len(encrypted_text), 16))
print (decrypted_text)
