# Exercice 7
# En Python, créer un programme qui calcule et affiche la somme des lignes d’une matrice aléatoire de deux manières différentes.

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

# Calculer et afficher la somme des lignes de la matrice (première méthode)
print("Somme des lignes de la matrice (première méthode) :")
for ligne in matrice:
    somme = sum(ligne)
    print(somme)

# Calculer et afficher la somme des lignes de la matrice (deuxième méthode)
print("Somme des lignes de la matrice (deuxième méthode) :")
for i in range(n):
    somme = 0
    for j in range(m):
        somme += matrice[i][j]
    print(somme)
