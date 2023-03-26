# Exercice 11
# En Python, créer un programme qui calcule et affiche la transposée d’une matrice aléatoire. La matrice de départ et sa transposée sont affichées à l’écran.

import random

# Définir la taille de la matrice
n = int(input("Entrez la taille de la matrice : "))

# Créer une matrice aléatoire
matrice = []
for i in range(n):
    ligne = []
    for j in range(n):
        element = random.randint(0, 10)
        ligne.append(element)
    matrice.append(ligne)

# Afficher la matrice
print("Matrice :")
for ligne in matrice:
    print(ligne)

# Calculer la transposée de la matrice
transposee = [[matrice[j][i] for j in range(n)] for i in range(n)]

# Afficher la transposée de la matrice
print("Transposée :")
for ligne in transposee:
    print(ligne)
