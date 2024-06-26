import math
def addition():
    A = []
    while True:
        ask = int(input("------------------\n'0' Pour leave\nSaisiez des nombres à additioner : "))
        if ask == 0:
            break
        A.append(ask)
    formule = sum(A)
    print(f"La somme des nombres suivant {A} est de {formule}")

def soustraction():
    A = int(input("Veuillez saisir un premier nombre :"))
    B = int(input("Veuillez saisir un deuxième nombre :"))
    result = A - B
    print(f"Le résultat de la soustraction {A} - {B} est de : {result}")
def multiply():
    A = int(input("Veuillez saisir un premier nombre :"))
    B = int(input("Veuillez saisir un deuxième nombre :"))
    result = A * B
    print(f"Le résultat de la multiplication {A} * {B} est de : {result}")
def divise():
    ask = int(input("--------------------\n1. Division classique\n2. Division euclidienne"))
    if ask ==1:
        A = int(input("Veuillez saisir un premier nombre :"))
        B = int(input("Veuillez saisir un deuxième nombre :"))
        result = A / B
        print(f"Le résultat de la division classique {A} / {B} est de : {result}")
    elif ask ==2:
        A = int(input("Veuillez saisir un premier nombre :"))
        B = int(input("Veuillez saisir un deuxième nombre :"))
        result = A % B
        print(f"Le résultat de la division euclidienne {A} / {B} est de : {result}")
def racine():
    Ra = int(input("Entrez un nombre : "))
    if Ra > 0:
        print(math.sqrt(Ra))
    if Ra < 0:
        print("Il n'est pas possible d'effectuer la racine carré d'un nombre négatif car elle n'existe pas")
def power():
    askP = int(input("Veuillez entrez un nombre"))
    askE = int(input(f"Veuillez saisir la puissance du chiffre {askP}"))
    result = pow(askP, askE)
    print(result)