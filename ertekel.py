import random

def ertekeles():
    etel_nev:str = input("Étel neve: ")
    rendelo_neve:str = input("Étel rendelőjének neve: ")
    ertekeles:int = int(input("Értékelés (1-5): "))
    i = 0
    while(i < 1):
        if (1 <= ertekeles <= 5):
            i += 1
            print("\nI/C:\nKöszönjük az értékelést!")
        elif (ertekeles < 0):
            print("Az értékelés nem lehet negatív!")
            ertekeles:int = int(input("Értékelés (1-5): "))
        elif (ertekeles > 5):
            print("5 pont feletti értékelés nem elfogadható!")
            ertekeles:int = int(input("Értékelés (1-5): "))