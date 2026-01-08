import random

pismena = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

random.shuffle(pismena)
abeceda = pismena[:6]

tajne = abeceda[:4]
random.shuffle(abeceda)

hracove = len(tajne)*'-'
pokusy = 10

# info pre mna
print('tvoja abeceda pre tuto hru je: ')
print(*abeceda,sep = ',')
print(tajne)

while pokusy > 0 and ('-' in hracove or 'x' in hracove):
    slovo = input('zadaj 4 pismenne slovo: ')
    nove = []
    su_vsetky_pismenka_v_abecede = True
    for s in slovo:
        if not s in abeceda:
            su_vsetky_pismenka_v_abecede = False
    if su_vsetky_pismenka_v_abecede:
        if len(slovo) == 4:
            for i in range(len(slovo)):
                s = slovo[i]
                t = tajne[i]
                if s == t:
                    nove.append('X')
                elif s in tajne:
                    nove.append('x')
                else:
                    nove.append('-')
            pokusy -= 1
            hracove = nove
            print(hracove)
        elif len(slovo) > 4:
            print('zadane slovo je prilis dlhe')
        elif len(slovo) < 4:
            print('zadane slovo je prilis kratke')
    else:
        print('pouzil si nepouzitelne pismenka')

if pokusy == 0:
    print('NEUHADOL SI :(')
    print('TAJNE SLOVO BOLO: ' + str(tajne))
else:
    print('UHADOL SI :)')
