import ertekel
import sorozat
import poggyasz1

print("I/A, B:")
ertekel.ertekeles()

print("\nII/A, B, C:")
lista = sorozat.vel_sorozat()
str_sorozat = sorozat.sorozat_str(lista)
print(str_sorozat)

#II/D,E
db = sorozat.paratlan(lista)
sorozat.konzol_kiir(db)

#II/F
sorozat.fajlba_kiir(db)

#III
lista = poggyasz1.beolvasas()
poggyasz1.poggyaszok(lista)
poggyasz1.atlag_tomeg(lista)
poggyasz1.legm_poggy(lista)