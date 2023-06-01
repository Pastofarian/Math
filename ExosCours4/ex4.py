# Ecrivez un programme qui inverse une matrice par la méthode du pivot de Gauss-Jordan (vous
# aurez besoin des programmes des exercices 1 et 2 sous forme de fonction)
# (Vous trouverez une description complète de l’algorithme en pseudo-code sur la diapo suivante)
# (On cherche le max de la première colonne comme premier pivot et si il ne se trouve pas en a11,
# on l’y met en échangeant la ligne du max avec la première. On divise la ligne par la valeur du max
# pour obtenir 1, puis on s’occupe de a12 et ainsi de suite on descend jusqu’au bout de la colonne,
# puis on passe à la colonne suivante on cherche le max, on le met par échange sur la diagonale et
# on s’occupe des valeurs du dessous et du dessus dans la colonne 2 et on passe à la colonne
# suivante etc.)

# Soit une matrice A de dimensions n × m ;
# L'algorithme de Gauss-Jordan en Pseudo-code est le suivant:
# r = 0 (r est l'indice de ligne du dernier pivot trouvé)
# Pour j de 1 jusqu'à m (j décrit tous les indices de colonnes)
# | Rechercher max(|A[i,j]|, r+1 ≤ i ≤ n). Noter k l'indice de ligne du maximum
# | (A[k,j] est le pivot)
# | Si A[k,j]≠0 alors (A[k,j] désigne la valeur de la ligne k et de la colonne j)
# | | r=r+1 (r désigne l'indice de la future ligne servant de pivot)
# | | Diviser la ligne k par A[k,j] (On normalise la ligne de pivot de façon que le pivot prenne la valeur 1)
# | | Si k≠r alors
# | | | Échanger les lignes k et r (On place la ligne du pivot en position r)
# | | Fin Si
# | | Pour i de 1 jusqu'à n (On simplifie les autres lignes)
# | | | Si i≠r alors
# | | | | Soustraire à la ligne i la ligne r multipliée par A[i,j] (de façon à annuler A[i,j])
# | | | Fin Si
# | | Fin Pour
# | Fin Si
# Fin Pour
# Fin Gauss-Jordan

import numpy as np


def swap_rows(A, i, j):
    A[[i, j]] = A[[j, i]]
    return A


def transvection(A, k, i, alpha):
    """
    On fait l'opération de transvection sur la matrice A
    On soustrait (alpha fois la ligne i ) de la ligne k
    """
    A[k, :] = A[k, :] - alpha * A[i, :]
    return A


def Gauss_Jordan_inverse(A):
    m, n = A.shape
    if m != n:
        raise ValueError("La matrice doit être carrée")

    # On augmente la matrice A avec la matrice identité (On concatène la matrice identité de la même taille que A à la droite de A)
    A = np.hstack([A, np.identity(n)])

    for j in range(n):
        # trouve la ligne pivot et inverse si nécéssaire
        pivot_row = max(range(j, m), key=lambda i: abs(A[i, j]))
        if pivot_row != j:
            A = swap_rows(A, j, pivot_row)

        # On normaliser la ligne pivot (On divise la ligne pivot par l'élément pivot pour qu'il devienne 1)
        A[j, :] = A[j, :] / A[j, j]

        # Elimine les autres entrée dans la colonne en cours
        for i in range(m):
            if i != j:
                A = transvection(A, i, j, A[i, j])

    # On extrait la matrice inverse
    A_inv = A[:, n:]

    return A_inv


A = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])

# Calcule l'inverse de A
A_inv = Gauss_Jordan_inverse(A)

print("A:")
print(A)
print("\nA_inv:")
print(A_inv)
print("\nA * A_inv:")
print(np.dot(A, A_inv))
