# Exercice 1
"""
# En Python, créer un programme qui génère une matrice aléatoire dont les éléments sont des entiers et un autre où ce sont des réels. La taille de la matrice est entrée au clavier. Le résultat est affiché proprement à l’écran

import random

# Demander la taille de la matrice à l'utilisateur
taille = int(input("Entrez la taille de la matrice : "))

# Générer une matrice aléatoire d'entiers
matrice_entiers = [
    [random.randint(0, 100) for j in range(taille)] for i in range(taille)
]
print("Matrice d'entiers aléatoires :")
for ligne in matrice_entiers:
    print(ligne)


###########Autre façon de générer une matrice aléatoire d'entiers#########################
matrice_entiers = []
for i in range(taille):
    ligne = []
    for j in range(taille):
        # print("j = {}".format(j))
        ligne.append(random.randint(0, 100))
    matrice_entiers.append(ligne)

print("Matrice d'entiers aléatoires :")
for i in range(taille):
    for j in range(taille):
        print(matrice_entiers[i][j], end=" ")
    print()


# Générer une matrice aléatoire de réels
matrice_reels = [
    [round(random.uniform(0, 1), 2) for j in range(taille)] for i in range(taille)
]
print("Matrice de réels aléatoires :")
for ligne in matrice_reels:
    print(ligne)

"""
import numpy as np

# On demande la taille de la matrice comme input
n = int(input("Entrez la taille de la matrice : "))

# On crée une matrice random int entre 0 et 10
matrice_entiers = np.random.randint(low=0, high=10, size=(n, n), dtype=int)

# On crée une matrice random de nombres réels entre 0 et 1
matrice_reels = np.random.rand(n, n)

# Afficher les matrices
print("Matrice d'entiers :")
print(matrice_entiers)
print("Matrice de nombres réels :")
print(matrice_reels)
