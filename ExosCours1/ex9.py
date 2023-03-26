# Exercice 9
# En Python, créer un programme qui calcule et affiche la nème puissance d’une matrice carrée aléatoire de manière « économique »

import random

# Définir la taille de la matrice carrée
n = int(input("Entrez la taille de la matrice carrée : "))

# Créer une matrice carrée aléatoire
matrice = []
for i in range(n):
    ligne = []
    for j in range(n):
        element = random.randint(0, 10)
        ligne.append(element)
    matrice.append(ligne)

# Afficher la matrice carrée
print("Matrice carrée aléatoire :")
for ligne in matrice:
    print(ligne)

# Demander à l'utilisateur de saisir la puissance à laquelle élever la matrice
puissance = int(input("Entrez la puissance de la matrice : "))

# Initialiser la matrice résultat
resultat = [[int(i == j) for j in range(n)] for i in range(n)]

# Calculer la nème puissance de la matrice carrée en utilisant l'algorithme de l'exponentiation rapide
while puissance > 0:
    if puissance % 2 == 1:
        # Multiplier la matrice résultat par la matrice carrée
        nouveau_resultat = []
        for i in range(n):
            ligne = []
            for j in range(n):
                element = 0
                for k in range(n):
                    element += resultat[i][k] * matrice[k][j]
                ligne.append(element % 10)
            nouveau_resultat.append(ligne)
        resultat = nouveau_resultat

    # Élever la matrice carrée au carré
    nouvelle_matrice = []
    for i in range(n):
        ligne = []
        for j in range(n):
            element = 0
            for k in range(n):
                element += matrice[i][k] * matrice[k][j]
            ligne.append(element % 10)
        nouvelle_matrice.append(ligne)
    matrice = nouvelle_matrice

    # Diviser la puissance par 2
    puissance //= 2

# Afficher la matrice résultat
print("Matrice résultat :")
for ligne in resultat:
    print(ligne)


# Ce programme demande d'abord la taille d'une matrice carrée. Ensuite, il crée une matrice carrée avec des nombres aléatoires et l'affiche. Après, il demande la puissance à utiliser. Il commence avec une matrice identité et calcule la puissance de la matrice en utilisant une méthode "algorithme de l'exponentiation rapide". Il divise la puissance par 2 à chaque étape et fait les multiplications nécessaire. Il utilise le modulo 10 pour limiter la taille des nombres. À la fin, il devrait afficher la matrice en résultat mais ce n'est pas correcte.
