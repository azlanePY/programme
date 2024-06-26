import math
import calculFonction
def perimeter_circle():
    ask = int(input("Quel est le rayon du cercle ?"))
    formule = (2 * ask) * math.pi
    print(f"Le rayon du cercle est de {formule}")
def moyenne():
    L = []
    for i in range(0, 11):
        note = int(input(f"Veuillez entre la note numéro {i} :\nPour annuler entrez '0' "))
        if note == 0:
            break
        L.append(note)
    print(f"Voici la série de note {L}")
    formule = sum(L) / len(L)
    print(f"La moyenne de la liste est de {formule}")
def calculatrice():
    C = int(input("1. Addition\n2. Soustraction\n3.Multiplication\n4. Divsion\n5. Racine carré d'un nombre\n6. Puissance d'un nombre\nVeuillez choisir une opération : "))
    if C ==1:
        calculFonction.addition()
    if C ==2:
        calculFonction.soustraction()
    if C ==3:
        calculFonction.multiply()
    if C ==4:
        calculFonction.divise()
    if C==5:
        calculFonction.racine()
    if C==6:
        calculFonction.power()
def pair_imapir():
    N = int(input("Saisir un nombre :"))
    if N % 2 ==0:
        print(f"Le chiffre {N} est pair")
    if N % 2 !=0:
        print(f"Le chiffre {N} est impair")
