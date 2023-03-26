# Exercice 8
# En Python, créer un programme qui calcule et affiche la somme des colonnes d’une matrice aléatoire de deux manières différentes.

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

# Calculer et afficher la somme des colonnes de la matrice (première méthode)
print("Somme des colonnes de la matrice (première méthode) :")
for j in range(m):
    somme = 0
    for i in range(n):
        somme += matrice[i][j]
    print(somme)

# Calculer et afficher la somme des colonnes de la matrice (deuxième méthode)
print("Somme des colonnes de la matrice (deuxième méthode) :")
for j in range(m):
    colonne = [matrice[i][j] for i in range(n)]
    somme = sum(colonne)
    print(somme)
