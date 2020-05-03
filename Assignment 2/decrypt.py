
from struct import pack, unpack

strg = '{}'

def F(w):
    return ((w * 31337) ^ (w * 1337 >> 16)) % 2**32
''' 
   Return the original text after decrypting it
'''

def decrypt(block):    
    a, b, c, d = unpack('<4I', block)
    for i in range(32):       
        tmp = a
        d = d ^ 1337
        a = c ^ (F(d | F(d) ^ d))
        b = b ^ (F(d ^ F(a) ^ (d | a)))
        c = tmp ^ (F(d | F(b ^ F(a)) ^ F(d | b) ^ a))
        
        tmp = a
        a = d ^ 31337
        d = c ^ (F(a | F(a) ^ a))
        c = b ^ (F(a ^ F(d) ^ (a | d)))
        b = tmp ^ (F(a | F(c ^ F(d)) ^ F(a | c) ^ d))
    
    pk = pack('<4I', a, b, c, d)
    return pk 
      
''' 
    Open the "flag.enc" file in binary format "rb" mode for reading 
    iterate over every 16 bytes of the ciphertext and print out the original text
 '''
enc = open('flag.enc','rb').read()

def edit_text(txt):
    new_str = strg.format(txt)[2:-1]
    return new_str
    

dec = "".join(edit_text(decrypt(enc[i:i+16])) for i in range(0,len(enc), 16))
print (dec)