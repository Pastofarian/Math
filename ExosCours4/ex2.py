# Ecrivez un programme qui soustrait d'une ligne k un multiple d'une autre ligne d'une
# matrice (transvection: Lk = Lk – alpha.Li) et qui sera appelé par l'instruction
# nom-fonction(A,k,i,alpha) où A est le nom de la matrice et k et i le numéro des lignes
# à soustraire et alpha le facteur de multiplication de la i
# ème ligne avant soustraction

import numpy as np


def transvection(A, k, i, alpha):
    """
    On fait l'opération de transvection sur la matrice A
    On soustrait (alpha fois la ligne i ) de la ligne k
    """
    A[k, :] = A[k, :] - alpha * A[i, :]
    return A


A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# transvection sur la ligne 1 et 2 avec l'alpha = 2
A = transvection(A, 1, 2, 2)

print(A)
