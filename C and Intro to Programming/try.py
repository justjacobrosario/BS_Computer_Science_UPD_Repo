str = '''
Zee Angsuco
8:43 AM
Zee M. Angsuco, PPCES, Jocelyn S. Cruz, English

Carljeff
8:44 AM
Carljeff T. Abagon PPCES Jocelyn S. Cruz Filipino

Bry Delgado
8:44 AM
BYRLLE I DELGADO, HHIS, MA ROSSEL LAO,ENGLISH

Zia Ann Alexa Cagadas
8:44 AM
ZIA ANN ALEXA C. CAGADAS, ERIS, ERMA D. GUERRERO, FIL

Merchanz Acetrylle
8:44 AM
Merchanz Acetrylle F. Fajilan, MES, Genel D. Veluz, English

Aimhiel Urbino
8:46 AM
YEN AIMHIEL U. ANGELITO,PHES, MANUELITO M. BERMUDEZ,ENGLISH

Rolando Eli Luis Reyes
8:46 AM
Rolando Eli Luis P. Reyes, HHIS, Encar Colet, Filipino

Dhapny faith Eslabon
8:47 AM
Dhapny Faith Eslabon, Highway Hills Integrated School,Maria Rossel C Lao,English

Valkyrie Baylon
8:47 AM
Valkyrie F. Baylon, HIS, Ma. Elizabeth T. Mateo, Filipino

ricashanemaglaque28@gmail.com
8:48 AM
Rica Shane j.  Maglaque,HIS, Mrs. Elizabeth T. Mateo, Filipino

REVELYN DANAO
8:51 AM
Marvelyn Renee T. Danao, MES, Genel D. Veluz, English

Carl Xander Magpantay
8:52 AM
Carl Xander C Magpantay HHIS SPA ENCAR B. COLET FILIPINO

John
8:57 AM
Bernard Gregory Tolentino, Hhis Maam Lao, ENG

Llannz Yurie Ramilo
8:57 AM
Llannz Yurie D. Ramilo - M.E.S. - Ma'am Fadriquela - FIL

Joy Anne Balesa
9:01 AM
Francheska Jade M. Balesa,- PES- Shiela Marie G. Destura - English

Joice Tucay
9:05 AM
Joice Lee Q. TUCAY - P.H E.S - Ma'am Esther - ENGLISH

Erica Marie Vicaran
9:09 AM
Erica Marie D. Vicaran - MES - Ma'am Fadriquela - Fil
'''

def fast_pow(n, expo):
    if expo == 0:
        return 1
    elif (expo%2 == 0):
        return (fast_pow(n, expo/2))**2
    else:
        return n * (fast_pow(n, (expo-1)/2))**2

memo = {}
def memo_fast_pow(n, expo):

    if expo in memo:
        return memo[expo]
    else:

        if expo == 0:
            memo[expo] = 1
            return memo[expo]

        elif (expo%2 == 0):
            memo[expo] = (fast_pow(n, expo/2))**2
            return memo[expo]
        else:
            memo[expo] = n * (fast_pow(n, (expo-1)/2))**2
            return memo[expo]
            
n = 2318
e = 1099

print(n**e)

print(fast_pow(n, e))

print(memo_fast_pow(n, e))



