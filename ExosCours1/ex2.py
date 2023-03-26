# Exercice 2

# En Python, créer un programme qui génère une matrice unité, une matrice diagonale, une matrice triangulaire, une matrice creuse, une matrice nulle. La taille de la matrice est entrée au clavier
"""
# Demande la taille de la matrice à l'utilisateur
n = int(input("Entrez la taille de la matrice : "))

# Crée une matrice unité
matrice_unite = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
print("Matrice unité :")
for ligne in matrice_unite:
    print(ligne)

# Crée une matrice diagonale
matrice_diagonale = [[i + 1 if i == j else 0 for j in range(n)] for i in range(n)]
print("Matrice diagonale :")
for ligne in matrice_diagonale:
    print(ligne)

# Crée une matrice triangulaire
matrice_triangulaire = [[0 if i < j else i + j for j in range(n)] for i in range(n)]
print("Matrice triangulaire :")
for ligne in matrice_triangulaire:
    print(ligne)

# Crée une matrice creuse
matrice_creuse = [
    [1 if i == j else 2 if i == j - 1 or i == j + 1 else 0 for j in range(n)]
    for i in range(n)
]
print("Matrice creuse :")
for ligne in matrice_creuse:
    print(ligne)

# Crée une matrice nulle
matrice_nulle = [[0 for j in range(n)] for i in range(n)]
print("Matrice nulle :")
for ligne in matrice_nulle:
    print(ligne)
"""


import numpy as np

# Demande la taille de la matrice à l'utilisateur
n = int(input("Entrez la taille de la matrice : "))

# Crée une matrice unité
matrice_unite = np.eye(n)
print("Matrice unité :\n", matrice_unite)

# Crée une matrice diagonale
matrice_diagonale = np.diag(np.arange(1, n + 1))
print("Matrice diagonale :\n", matrice_diagonale)

# Crée une matrice triangulaire
matrice_triangulaire = np.tril(np.random.rand(n, n))
print("Matrice triangulaire :\n", matrice_triangulaire)

# Crée une matrice creuse
matrice_creuse = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i == j:
            matrice_creuse[i, j] = 1
        elif i == j - 1 or i == j + 1:
            matrice_creuse[i, j] = 2
print("Matrice creuse :\n", matrice_creuse)

# Crée une matrice nulle
matrice_nulle = np.zeros((n, n))
print("Matrice nulle :\n", matrice_nulle)
