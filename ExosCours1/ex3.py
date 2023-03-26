# Exercice 3
# En Python, créer un programme qui additionne/soustrait deux matrices après avoir vérifié que l’addition est possible. Les matrices sont entrées au clavier élément par élément.

"""
# Demander la taille des matrices à l'utilisateur
n = int(input("Entrez le nombre de lignes des matrices : "))
m = int(input("Entrez le nombre de colonnes des matrices : "))

# Initialiser les matrices
matrice1 = []
matrice2 = []
resultat = []

# Demander à l'utilisateur de saisir les éléments des matrices
print("Saisissez les éléments de la première matrice :")
for i in range(n):
    ligne = []
    for j in range(m):
        element = float(input("Entrez l'élément ({}, {}) : ".format(i + 1, j + 1)))
        ligne.append(element)
    matrice1.append(ligne)

print("Saisissez les éléments de la deuxième matrice :")
for i in range(n):
    ligne = []
    for j in range(m):
        element = float(input("Entrez l'élément ({}, {}) : ".format(i + 1, j + 1)))
        ligne.append(element)
    matrice2.append(ligne)

# Vérifier si l'addition est possible
operation = input("Voulez-vous faire une addition (+) ou une soustraction (-) ? ")
if (
    operation == "+"
    and matrice1 != []
    and matrice2 != []
    and len(matrice1) == len(matrice2)
    and len(matrice1[0]) == len(matrice2[0])
):
    # Effectuer l'addition des deux matrices
    for i in range(n):
        ligne = []
        for j in range(m):
            element = matrice1[i][j] + matrice2[i][j]
            ligne.append(element)
        resultat.append(ligne)
    # Afficher le résultat
    print("Le résultat de l'addition est :")
    for ligne in resultat:
        print(ligne)
elif (
    operation == "-"
    and matrice1 != []
    and matrice2 != []
    and len(matrice1) == len(matrice2)
    and len(matrice1[0]) == len(matrice2[0])
):
    # Effectuer la soustraction des deux matrices
    for i in range(n):
        ligne = []
        for j in range(m):
            element = matrice1[i][j] - matrice2[i][j]
            ligne.append(element)
        resultat.append(ligne)
    # Afficher le résultat
    print("Le résultat de la soustraction est :")
    for ligne in resultat:
        print(ligne)
else:
    # Afficher un message d'erreur si l'opération n'est pas possible
    print("L'addition ou la soustraction n'est pas possible avec ces matrices.")

"""
import numpy as np

# Demander la taille des matrices
n = int(input("Entrez la taille des matrices : "))

# Initialiser les matrices
matrice1 = np.zeros((n, n))
matrice2 = np.zeros((n, n))

# Saisir les éléments des matrices
print("Entrez les éléments de la première matrice :")
for i in range(n):
    for j in range(n):
        matrice1[i, j] = float(input(f"Element ({i}, {j}) : "))

print("Entrez les éléments de la deuxième matrice :")
for i in range(n):
    for j in range(n):
        matrice2[i, j] = float(input(f"Element ({i}, {j}) : "))

# Vérifier que les deux matrices ont la même taille
if matrice1.shape != matrice2.shape:
    print(
        "Erreur : Les matrices doivent être de même taille pour être additionnées ou soustraites."
    )
else:
    # Additionner les matrices
    somme = matrice1 + matrice2
    print("Somme des matrices :")
    print(somme)

    # Soustraire les matrices
    difference = matrice1 - matrice2
    print("Différence des matrices :")
    print(difference)
