# # Ecrivez un programme qui calcule le déterminant d’une matrice par la méthode du pivot
# # de Gauss_Jordan (vous aurez besoin des programmes des exercices 1 et 2 sous forme de
# # fonction)

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


def Gauss_Jordan(A):
    """
    on retourne une matrice triangulaire supérieure, tous les éléments en dessous de la diagonale son null
    """
    m, n = A.shape
    for j in range(n):
        # trouve la ligne pivot et inverse si nécéssaire
        pivot_row = max(range(j, m), key=lambda i: abs(A[i, j]))
        if pivot_row != j:
            A = swap_rows(A, j, pivot_row)

        # Elimine les autres entrées dans la colonne en cours
        for i in range(j + 1, m):
            if A[j, j] != 0:
                A = transvection(A, i, j, A[i, j] / A[j, j])
    return A


def determinant(A):
    """
    Calcule le determinant de la matrice A avec Gauss_Jordan
    """
    m, n = A.shape
    if m != n:
        raise ValueError("La matrice doit être carrée")

    # Applique la fonction pour obtenir la forme échelonnée (matrice triangulaire supérieure)
    U = Gauss_Jordan(A)

    # Le determinant est le produit des éléments de la diagonale de U
    det = np.prod(np.diag(U))

    return det


A = np.array([[1, 3, 3, 1], [1, 4, 3, 0], [1, 3, 4, 2], [2, 1, 0, 1]])

det = determinant(A)

print(det)

# On obtient 0 car la matrice donnée est ce qu'on appelle une matrice singulière, c'est-à-dire qu'elle n'a pas d'inverse. Une matrice qui n'a pas d'inverse a un déterminant égal à zéro.
