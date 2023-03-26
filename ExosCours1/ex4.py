# Exercice 4
# En Python, créer un programme qui crée une matrice aléatoire, qui calcule ensuite son opposée, affiche les deux matrices et qui vérifie que leur somme fait bien … (à compléter par vous-même) une matrice nulle.
"""
import random

# Définir la taille de la matrice
n = int(input("Entrez le nombre de lignes de la matrice : "))
m = int(input("Entrez le nombre de colonnes de la matrice : "))

# Créer une matrice aléatoire
matrice = []
for i in range(n):
    ligne = []
    for j in range(m):
        element = random.randint(0, 10)
        ligne.append(element)
    matrice.append(ligne)

# Afficher la matrice
print("Matrice aléatoire :")
for ligne in matrice:
    print(ligne)

# Calculer l'opposée de la matrice
opposee = []
for i in range(n):
    ligne = []
    for j in range(m):
        element = -matrice[i][j]
        ligne.append(element)
    opposee.append(ligne)

# Afficher l'opposée de la matrice
print("Opposée de la matrice :")
for ligne in opposee:
    print(ligne)

# Vérifier que la somme des deux matrices fait zéro
somme = []
for i in range(n):
    ligne = []
    for j in range(m):
        element = matrice[i][j] + opposee[i][j]
        ligne.append(element)
    somme.append(ligne)

# Afficher la somme des deux matrices
print("Somme de la matrice et de son opposée :")
for ligne in somme:
    print(ligne)

# Vérifier si la somme est égale à une matrice nulle
est_nulle = True
for i in range(n):
    for j in range(m):
        if somme[i][j] != 0:
            est_nulle = False
            break

if est_nulle:
    print("La somme de la matrice et de son opposée est égale à une matrice nulle.")
else:
    print(
        "La somme de la matrice et de son opposée n'est pas égale à une matrice nulle."
    )
"""
import numpy as np

# Demander la taille de la matrice aléatoire
n = int(input("Entrez la taille de la matrice : "))

# Générer la matrice aléatoire d'entiers
matrice_entiers = np.random.randint(10, size=(n, n))

# Calculer l'opposée de la matrice
matrice_opposee = -matrice_entiers

# Afficher les deux matrices
print("Matrice aléatoire d'entiers :")
print(matrice_entiers)
print("Matrice opposée :")
print(matrice_opposee)

# Vérifier que la somme de la matrice et de son opposée est nulle
matrice_nulle = np.zeros((n, n))
somme = matrice_entiers + matrice_opposee
if np.array_equal(somme, matrice_nulle):
    print("La somme de la matrice et de son opposée est bien la matrice nulle.")
else:
    print("La somme de la matrice et de son opposée n'est pas la matrice nulle.")
