# Solving [genfei challenge]( https://cybertalents.com/challenges/cryptography/genfei ) on cybertalents using Python
> a cryptography challenge that try to hack ciphers (medium level)

## Included files details :
#### 1. cybertalents profile file :
- a screenshot from cybertalents account profile 

#### 2. output test file:
- a screenshot from the output on spyder platform

#### 3. falg.enc file :
- Is a given file that contains a copy of the encrypted string returned during encryption

#### 4. encrypt.py file :
- Is a given file that represent the stage that converts a plaintext into a ciphertext. <br/>
**This file** encrypts a number of bytes = (4*4) at a time , 
and return a new string representing an encrypted set of bytes , using XOR operation

> Note : XOR is a logical operation that can only be applied to (int) numbers ,
then the block of bytes is first converted into intergers (unpack) then again converted to bytes at the end of the whole XORing(encryption) , to be saved to the flag file (pack).

#### 5. decrypt.py file :
- This is the stage that converts the ciphertext returned during encryption into the plaintext. <br/>
**This file** decrypts a number of bytes and return the plaintext as a string , ending with "###" , using the reverse operation used in encryption , which will be XOR.

> Again the block of bytes is first converted into (int) numbers to be decrypted using XOR , then return a string of bytes to be printed out 

<br/>
<br/>

### For more challenges
please visit [cryptography challenges]( https://cybertalents.com/challenges/cryptography )


