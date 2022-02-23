#1

"""
1.1 Feladat
Készíts egy programot, amely a felhasználótól számokat kér be mindaddig, amíg az csupán ENTER-t nem üt! A számokat tárolja el a program egy listában! Az adatbekérés befejezte után írja ki a program a lista elemeit, a legkisebb és a legnagyobb számot!
"""

"""
lista = []
while True:
    szam = input("kérek egy szamot: ")
    if szam == "":
        break
    else:
        szam = int(szam)
        lista.append(szam)

print(lista)

legkisebb = lista[0]
for i in lista:
    if i < legkisebb:
        legkisebb = i

legnagyobb = lista[0]
for i in lista:
    if i > legnagyobb:
        legnagyobb = i
print(legnagyobb)

print("A legkisebb szám:", legkisebb, "\nA legnagyobb szám :", legnagyobb,"\nA lista pedig:", lista)   
"""
#-------------------------------------------------

#2.

"""
1.2 Feladat
Alakítsd át úgy az előbbi programot, hogy az 'X' vagy 'x' megadása eredményezze az adatbekérés végét!
"""

"""
lista = []
while True:
    szam = input("kérek egy szamot: ")
    if szam == "x" or szam =="X":
        break
    else:
        szam = int(szam)
        lista.append(szam)

print(lista)

legkisebb = lista[0]
for i in lista:
    if i < legkisebb:
        legkisebb = i

legnagyobb = lista[0]
for i in lista:
    if i > legnagyobb:
        legnagyobb = i
print(legnagyobb)

print("A legkisebb szám:", legkisebb, "\nA legnagyobb szám :", legnagyobb,"\nA lista pedig:", lista)   
"""

#----------------------------------------------------

#1.3

"""1.3 Feladat
Alakítsd át úgy az előbbi programot, hogy a legkisebb és legnagyobb páros számot határozza meg!
"""

"""
lista = []
while True:
    szam = input("kérek egy szamot: ")
    if szam == "x" or szam =="X":
        break
    else:
        szam = int(szam)
        lista.append(szam)



legkisebb = lista[0]
for i in lista:
    if i < legkisebb and i % 2 == 0:
        legkisebb = i

legnagyobb = lista[0]
for i in lista:
    if i > legnagyobb and i % 2 == 0:
        legnagyobb = i
print(legnagyobb)

print("A legkisebb páros szám:", legkisebb, "\nA legnagyobb páros szám :", legnagyobb,"\nA lista pedig:", lista)
"""

#--------------------------------------------------------

#2.

"""
2. Feladat
Készíts egy programot, amely a felhasználótól szavakat kér be, amíg az csupán ENTER-t nem üt! A szavakat tárolja el a program egy listában! Az adatbekérés befejezte után írja ki a program a lista elemeit, a legrövidebb és a leghosszabb szót!
"""

lista = []

while True:    
    szavak = input("Kérek egy szót: ")
    lista.append(szavak)
    if szavak == "":
        break
lista.remove("")
legkisebb = lista[0]
for i in lista:
    if len(i) < len(legkisebb):
        legkisebb = i


legnagyobb = lista[0]
for i in lista:
    if len(i) > len(legnagyobb):
        legnagyobb = i
print(legnagyobb)
print(f"A legrövidebb szó a: {legkisebb} \n A legnaygobb szó pedig a:{legnagyobb}")