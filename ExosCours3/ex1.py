# 1.	Ecrire votre propre fonction/ programme qui fait la convolution entre une matrice de grande taille et un masque dont les noms sont passés en paramètre.

import numpy as np


def convolution(input_matrix, mask):
    # Prend les dimensions des inputs matrix et du mask
    i_rows, i_cols = input_matrix.shape
    m_rows, m_cols = mask.shape

    # Defini l'output
    output = np.zeros((i_rows, i_cols))

    # on pad des zeros
    pad_size = m_rows // 2
    padded = np.pad(input_matrix, pad_size, mode="constant", constant_values=0)

    # on boucle sur chaque case
    for i in range(pad_size, i_rows + pad_size):
        for j in range(pad_size, i_cols + pad_size):
            # extrait la sous matrice
            sub_matrix = padded[
                i - pad_size : i + pad_size + 1, j - pad_size : j + pad_size + 1
            ]

            # On multiplie la sous matrice et le mask
            result = sub_matrix * mask

            # additionne et assigne à l'output
            output[i - pad_size, j - pad_size] = np.sum(result)

    return output.astype(int)


input_matrix = np.array([[4, 5, 7, 8], [7, 5, 4, 1], [7, 8, 11, 2], [7, 6, 0, 0]])

mask = np.array(
    [
        [6, 0, 7],
        [7, 2, 1],
        [1, 0, 3],
    ]
)

output_matrix = convolution(input_matrix, mask)

print(output_matrix)
