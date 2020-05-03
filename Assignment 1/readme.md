> An encryption - decryption program  using shift, affine and vigenere ciphers ..
callable from the command line.

> Examples calls from terminal: <br/>
 ◦ solution.py affine dec input.txt output.txt a b <br/>
 ◦ solution.py shift enc input.txt output.txt a <br/>
 
### 1. Shift cipher :
#### **Encryption** <br/>

After applying the Shift Cipher with key K = 3 the plaintext **ABCDEFGHIJKLMNOPQRSTUVWXYZZZZAA** gaves us                          ciphertext **DEFGHIJKLMNOPQRSTUVWXYZABCCCCDD** <br/>
> For every letter in the **given** plaintext **ABCDEFGHIJKLMNOPQRSTUVWXYZZZZAA** :
> - Convert the letter into the number that matches its order in the alphabet starting from 0, and call this number X.
( A=0, B=1, C=2, ...,Y=24, Z=25)
> - Calculate **Y = (X + K) mod 26**
> - Convert the number Y into a letter that matches its order in the alphabet starting from 0.
(A=0, B=1, C=2, ...,Y=24, Z=25)  

####  **Decryption** <br/>
After decrypting the Shift Cipher with same key K , we deciphers the ciphertext **DEFGHIJKLMNOPQRSTUVWXYZABCCCCDD** into the original text **ABCDEFGHIJKLMNOPQRSTUVWXYZZZZAA**
> For every letter in the ciphertext **DEFGHIJKLMNOPQRSTUVWXYZABCCCCDD** :
> - Convert the letter into the number that matches its order in the alphabet starting from 0, and call this number Y.
(A=0, B=1, C=2, ..., Y=24, Z=25)
> - Calculate **X= (Y - K) mod 26**
> - Convert the number X into a letter that matches its order in the alphabet starting from 0.
(A=0, B=1, C=2, ..., Y=24, Z=25) <br/> 

<br/>

### 2. Affine cipher :
####  **Encryption** <br/>
After applying the Affine cipher , the plaintext **ABCDEFGHIJKLMNOPQRSTUVWXYZZZZAA** gave us ciphertext **INSXCHMRWBGLQVAFKPUZEJOTYDDDDII** <br/>
> - Using modular arithmetic to transform the integer that each plaintext letter corresponds to into another integer that correspond to a ciphertext letter. 
> - Calculate **E ( x ) = ( a x + b ) mod m** <br/>

####  **Decryption** <br/>
After applying the Affine cipher , the ciphertext **INSXCHMRWBGLQVAFKPUZEJOTYDDDDII** gave us plaintext  **ABCDEFGHIJKLMNOPQRSTUVWXYZZZZAA**  <br/>
> we perform the opposite (or inverse) functions on the ciphertext to retrieve the plaintext. <br/>
> - convert each of the ciphertext letters into their integer values. 
> - Use the decryption function **D ( x ) = a^-1 ( x - b ) mod m** <br/>

<br/>


### 3. Vigenere cipher :
It is a text encrypt/decrypt technique that uses a table of size 26x26 having the first row and first column , containing letters from A to Z and then each row has the letters shifted to the left one position. 

####  **Encryption** <br/>
After applying the Affine cipher , the plaintext **ABCDEFGHIJKLMNOPQRSTUVWXYZZZZAA** gave us ciphertext **CSASXNOJZHZEUVQGOGLBCXNVNSHHBRY**
> - pick a letter in the plaintext and its corresponding letter in the keyword
> - use the keyword letter and the plaintext letter as the row index and column index, respectively, and the entry at the row-column intersection is the letter in the ciphertext <r/>

####  **Decryption** <br/>
After applying the Affine cipher , the ciphertext  **CSASXNOJZHZEUVQGOGLBCXNVNSHHBRY** gave us plaintext **ABCDEFGHIJKLMNOPQRSTUVWXYZZZZAA** 
> - pick a letter in the ciphertext and its corresponding letter in the keyword
> - use the keyword letter to find the corresponding row, and the letter that contains the ciphertext letter is the needed plaintext letter. <br/>





