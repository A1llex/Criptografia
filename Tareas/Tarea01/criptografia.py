#import numpy as np
#Codigo decifrar vigenere
import numpy as np

""" 
Analisis de Frecuencias
"""
def frec(ctxt):
    letras = np.array(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
    frecuencias = np.arange(26)
    i = 0
    for c in ctxt:
        aux = ord(c)-ord('A')
        frecuencias[aux]+=1
        i+=1
    frecuencias = frecuencias/i
    frecuencias = list(zip(letras,frecuencias))
    frecuencias.sort(key=lambda x: -x[1])
    return frecuencias

#analisis de frecuencias
def kasiski(ctxt):
    seqSpacings = {}  # Keys are sequences; values are lists of int spacings.
    for seqLen in range(6, 12):
        for seqStart in range(len(ctxt) - seqLen):
            # Determine what the sequence is and store it in seq:
            seq = ctxt[seqStart:seqStart + seqLen]

            # Look for this sequence in the rest of the ctxt:
            for i in range(seqStart + seqLen, len(ctxt) - seqLen):
                if ctxt[i:i + seqLen] == seq:
                    # Found a repeated sequence:
                    if seq not in seqSpacings:
                        seqSpacings[seq] = []  # Initialize blank list.

                    # Append the spacing distance between the repeated
                    # sequence and the original sequence:
                    seqSpacings[seq].append(i - seqStart)
    return seqSpacings

#def modinv
def invmod(a,b): return 0 if a==0 else 1 if b%a==0 else b - invmod(b%a,a)*b//a

#Affine
def codeAffine(ptxt,key):
    a,b = key
    return ''.join([chr(
        ((( a*(ord(c)-ord('A')) + b ))%26 + ord('A')))  for c in ptxt ])

def decodeAffine (ctxt,key):
    a,b = key
    a_1 =  pow(a,-1,26)
    return ''.join([chr(((a_1*( (ord(c)-ord('A')) - b))%26 + ord('A')))  for c in ctxt ])

#Vigenere
def codeVignere(ptxt,key):
    return ''.join([chr(( ( (ord(c)-ord('A')) + (ord(key[i%len(key)])-ord('A')) ) % 26) + ord('A'))for i,c in enumerate(ptxt)])

def decodeVignere(ctxt,key):
    return ''.join([chr(( ( (ord(c)-ord('A')) - (ord(key[i%len(key)])-ord('A')) ) % 26) + ord('A'))for i,c in enumerate(ctxt)])


#Hill chiper
def codeHill(ptxt,key):
    key = np.array([(ord(c)-ord('A')) for c in key]).reshape(2,2)
    ptxt = np.array([(ord(c)-ord('A')) for c in ptxt])
    ptxt = ptxt.reshape(len(ptxt)//2,2)
    ctxt = np.dot(ptxt,key)%26
    return ''.join([chr(c+ord('A')) for c in ctxt.flatten()])

def decodeHill(ctxt,key):
    key = np.array([(ord(c)-ord('A')) for c in key]).reshape(2,2)
    key = np.linalg.inv(key)%26
    ctxt = np.array([(ord(c)-ord('A')) for c in ctxt])
    ctxt = ctxt.reshape(len(ctxt)//2,2)
    ptxt = np.dot(ctxt,key)%26
    return ''.join( [chr ( (  int(c))+ord('A') ) for c in ptxt.flatten()])

#Pruebas
#criptotexto4_hill = '''YQ QP PQ ZV WO NA LO ZS UX CD WU QQ SU UW HI NT MU SZ WM GO IO AN ZG WY BQ CS AE XR CF KT CD UM GW LO ZS HE PQ ZV KL WB VO XC ZV YQ NA OI SI QP ZG KP KQ WY LD WB UW DY KW UP WG QP MB MV AA VL MD QC RU LW SS UX RA ML AR IO RA RO CD TA LO ZS FC BI ER YD MD BQ RR MV KE OJ UI NT MV UR LO MW CD SC LD PQ HE CU LD UR EK OT AN XQ UP NI BK CS BW SC LD GZ UW YE QD AE LJ UW SZ RX ET UM HM CF QP KE IA HS ZG KP ZS JT WG UI LD CF SF UE WY BQ VM KW KE GE CX IO EG UP YQ KC GO AG QG IO SM CD ZG CD HI FR SS UX FS RR QP MW SC LD PQ UP ZS LO EI OJ VU GM AE RU DM XC NI SZ AN TW ZG DY FZ MB OA RK TK ZS QY XK SH SZ WB EH EG XK UX GZ YW AN SF MI AE MW IO SF SC TH AN CQ ZV OA YL FS ZS WU SI UW HI BL WM CU DC BC XV AM QK QK CD HS DM YD PQ FC CD UP GE FS UP NI BK CS BW MW TK OX IA QS AN ZG ZS QY XK SH AA PU TA CF QP GR MD HI PQ KP AA XV AR WGUW SC KQ VM RK TK BI FS UM CX EH SF MW RR IH MV WO RH AE RH CS MV CS XC ZV YQ NA GH PU RG HE SH TK NI BK CS BW CD UP LY TO WF DM LO ZS QF MI AE DY RK TK XW PQ LD EA DP YD OA UP AM CJ UE YL MW VH QP UP TQ UP GZ UP GR CQ RS UV AN ZG SC NA UV CQ EY CD TA SC KQ AO DM BI FS UM AN KE WM CJ QP KP FW GA TK SZ AT GK LO QS AN ZG CD QS AN ZG BI PQ GW LD CD SF YE FC CY UM UR GO AG QG XR ZS DC AN ZG QC UX VU LY BL UP GH WG KT OA CS QP MA QF QC PU JD AV CD MD JU TA KG PU BC CY VA MD KT YD UI FF MI AE RR IH EH SZ EH VU WU LO IP SS ZS GW DC EK FS HG IB CJ AN QF KY KT FV XC NI MV MU BW KW IH SF EG FZ UW KQ LD AN UW HI BL WM UT AR DS PQ LO LK GW MU AA RX AM SF CX KT MV UP YD QP LO TK LO QP EG JG KT AN LZ AI LD AN TA IP UP IO CD SM YD PQ OI VU AN CD YS LQ UX UR HS VM XK IO UR BC FR UP BQ IB SF UE KP KW OL WM OI NG QP ZS LY LO QY LO HG QP MA QF QC TO CW TE PY OI VU QC TB ET SZ LO ZS EV FS CS SD IO IA DC IC AE XC NI AN WG QP QY ZG XK CY ZD YW CD TA SZ OI HM DY ZV AR AN TA ZS CB JC GW MW GW NA LO XK KL KE UR UP LO MW KD QP SC YW RK TW VU AN ZS UX QP CQ IP KE XC ZV YQ NA CN'''
#hill = criptotexto4_hill.replace(" ", "")
prueba = "ENCANTOX"
Key = "BCDF"
codex = codeHill(prueba,Key)
print("CODIFICADO ",codex)
decodex = decodeHill(codex,Key)
print(decodex)

