# Ecrivez un programme qui inverse deux lignes d'une matrice et qui sera appelé par l'instruction
# nom-fonction(A,i,j) où A est le nom de la matrice et i et j le numéro des lignes à échanger

import numpy as np


def swap_rows(matrix, i, j):
    temp_row = matrix[i, :].copy()
    matrix[i, :] = matrix[j, :]
    matrix[j, :] = temp_row
    return matrix


# Example
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matrice originale:")
print(A)

i, j = 0, 1
swapped_matrix = swap_rows(A, i, j)
print(f"ligne inversée {i} et {j}:")
print(swapped_matrix)
