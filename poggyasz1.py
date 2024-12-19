from Poggyasz import Poggyasz
def beolvasas(fajlnev="csomag.txt"):
    poggyasz = []
    file = open(fajlnev, "r")
    sorok = file.readlines()
    file.close()
    fejléc = sorok[0]
    for i in range(1, len(sorok)):
        a, b, c, m = sorok[i].strip().split("#")
        poggyasz.append(Poggyasz(a, b, c, m))
    return poggyasz

def poggyaszok(poggyasz):
    print(f"\nIII/A, B:\nA poggyászok száma: {len(poggyasz)}")

def atlag_tomeg(poggyasz):
    ossz_t = 0
    db = 0
    for i in range(len(poggyasz)):
        if (poggyasz[i].a == 51):
            ossz_t += poggyasz[i].m
            db += 1
    print("\nIII/C:")
    if (db > 0):
        print(f"Az 51 cm-es poggyászok átlag tömeg értéke: {int((ossz_t / db) * 1000)}g")
    else:
        print("Nincs 51 cm-es poggyász.")

def legm_poggy(poggyasz):
    legm = poggyasz[0]  
    for i in range(1, len(poggyasz)):
        if (poggyasz[i].b > legm.b):
            legm = poggyasz[i]
    print(f"\nIII/D:\nA legmagasabb poggyász méretei: {legm.a}x{legm.b}x{legm.c}, tömege: {legm.m} kg.")