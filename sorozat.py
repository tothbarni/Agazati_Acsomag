import random

def vel_sorozat():
    lista = []
    for i in range(0, 12):
        szam:int = random.randint(-10, 1001)
        lista.append(szam)
    return lista

def sorozat_str(lista):
    str_sorozat:str = ""
    for i in range(0, len(lista)-1):
        str_sorozat += str(lista[i]) + "$"
    str_sorozat += str(lista[len(lista)-1])
    return str_sorozat

def paratlan(lista):
    db:int = 0
    for i in range(0, len(lista)-1):
        if (lista[i] % 2 == 1):
            db += 1
    return db

def konzol_kiir(db:int):
    print(f"\nII/F:\nA páratlanok száma: {db}")

def fajlba_kiir(db):
    f = open("eredmeny.txt","a")
    f.write(f"II/F:\nA páratlanok száma: {db}.")