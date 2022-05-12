import math
"""2b 06 2b 9e     fe
43 06 43 158"""

def decrypt(cipher, key): 
  #D(E) = (a^-1 * (E - b)) % 255
  print([(math.floor(key[0] * ord(c) - key[1])%256) for c in cipher])
  return ''.join([chr(math.floor(key[0] * ord(c) - key[1])%256)  for c in cipher ])
# Driver Code to test the above functions 


text0 = 'ÿØÿÛ'
text1 = 'ÿØÿà␀␐JFIF␀␁'
text2 = 'ÿØÿî'
text3 = 'ÿØÿá??Exif␀␀'
text4 = 'ÿØÿà'
text5 = '␀␀␀␌jP␠␠␍␊‡␊'
text6 = 'ÿOÿQ'
text7 = 'þíþí'

key = [(37/39), (2586/13)] 
key = [91, 182] 
#   # calling encryption function 
#   enc_text = encrypt(text, key) 
#   print('Encrypted Text: {}'.format(enc_text)) 
# calling decryption function 
print('Decrypted Text0: {}'.format(decrypt(text0, key) )) 
print('Decrypted Text1: {}'.format(decrypt(text1, key) )) 
print('Decrypted Text2: {}'.format(decrypt(text2, key) )) 
print('Decrypted Text3: {}'.format(decrypt(text3, key) )) 
print('Decrypted Text4: {}'.format(decrypt(text4, key) )) 
print('Decrypted Text5: {}'.format(decrypt(text5, key) )) 
print('Decrypted Text6: {}'.format(decrypt(text6, key) )) 
print('Decrypted Text7: {}'.format(decrypt(text7, key) )) 

