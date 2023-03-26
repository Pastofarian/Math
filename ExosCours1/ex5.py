# Exercice 5
# En Python, créer un programme qui exécute le produit d’une matrice aléatoire par un scalaire entré au clavier. La matrice de départ, le scalaire et le produit sont affichés à l’écran.
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

# Demander à l'utilisateur de saisir un scalaire
scalaire = float(input("Entrez un scalaire : "))

# Calculer le produit de la matrice par le scalaire
produit = []
for i in range(n):
    ligne = []
    for j in range(m):
        element = scalaire * matrice[i][j]
        ligne.append(element)
    produit.append(ligne)

# Afficher le scalaire et le produit de la matrice
print("Scalaire : {}".format(scalaire))
print("Produit de la matrice par le scalaire :")
for ligne in produit:
    print(ligne)

"""
import numpy as np

# Entrée de la taille de la matrice
n = int(input("Entrez la taille de la matrice : "))

# Création d'une matrice aléatoire
matrice = np.random.randint(0, 10, (n, n))
print("Matrice de départ : ")
print(matrice)

# Entrée du scalaire
scalaire = float(input("Entrez le scalaire : "))

# Produit matriciel avec le scalaire
produit = scalaire * matrice

# Affichage des résultats
print("Matrice résultat : ")
print(produit)
