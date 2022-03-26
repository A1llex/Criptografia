"""
2b 06 2b 9e fe
2b,06,2b,9e,fe = 43 6 43 158 254
                |-37|
---------------------------
fd ec bd b9
fd,ec,bd,b9 = 02 253   236     189     185
               |-04| 
                    |(-17)| +234
                        |(-47)|
"""     

"""
jpg a dec = 255 216 255 [219]
png 137 80 78 71 13
gif 71 73 70 56 55 97
78 85 82 85 73
105 99 110 115
73 73 42 0
128 42 95 215
78 85 82 85 73 77 71
83 68 80 88
88 80 68 83
118 47 49 1
70 79 82 77
207 132 1
82 73 70 70
"""

"""Music 
mp3 = 
255 251
255 243
255 242
73 68 51
82 73 70 70
102 76 97 67
70 79 82 77
"""

"""text ?
pdg 37 80 68 70 45
70 79 82 77
239 187 191
255 254
255 255
14 254 255
"""


arch1 =  open("file1.enc","rb")
arch2 =  open("file2.enc","rb")
arch3 =  open("file3.enc","rb")

filebytesA = bytearray()
filebytesB = bytearray()
filebytesC = bytearray()
cesar = "D4"

def cesar(x):
    return chr((ord(x)-ord('A')+10)%26+ord('A'))

def caesar_enc(plain, key):
    plain = plain.encode('utf-8')
    cipher = bytearray(plain)
    for i, c in enumerate(plain):
        cipher[i] = (c + key) & 0xff
    return bytes(cipher)

def caesar_dec(cipher, key):
    plain = bytearray(len(cipher))    # at most, len(plain) <= len(cipher)
    for i, c in enumerate(cipher):
        plain[i] = (c - key) & 0xff
    #return plain.decode('utf-8',errors='replace')
    return plain


filebytesA = bytearray(arch1.read(5))
print("A",filebytesA)
# for byte in filebytesA:
#     print( hex(byte)  )

filebytesB = bytearray(arch2.read())
print("B",filebytesB)
# for byte in filebytesB:
#     print(hex(byte))

# for i in range(256):
#     decodeed = caesar_dec(filebytesB, i)
#     print(f"Decode B key:{i} {decodeed.decode('utf-8',errors='ignore')}  en hex ={decodeed} ")
#     archivo = open(f"archivos/file{i}", 'wb+')
#     # for b in decodeed:
#     #     archivo.write(b)
#     archivo.write(decodeed)
#     archivo.close()

clave = 185
decodeed = caesar_dec(filebytesB, clave)
#print(f"Decode B key:{clave} {decodeed.decode('utf-8',errors='ignore')}  en hex ={decodeed} ")
archivo = open(f"file{clave}", 'wb+')
archivo.write(decodeed)
archivo.close()


"""
bytes: Es un arreglo (lista) de bytes, es decir, objetos de la clase bytes de python
nombre: string con el nombre del archivo a escribir / crear

def escribe_archivo(bytearr, nombre):
    archivo = open(nombre, 'wb')
        for b in bytearr:
        archivo.write(b)
    archivo.close( )

"""
#escribe_archivo([0x22, 0x25], "archivo") -> Crea un archivo llamado archivo con dos bytes.




