# 2.	Tester le bon fonctionnement en l’utilisant sur la matrice et le masque de l’exemple page 10 et 11 du syllabus sur les tenseurs.

import numpy as np


def convolution(input_matrix, mask):
    # Prend les dimension des inputs matrix et du mask
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


input_matrix = np.array([[2, 1, 3, 0], [1, 1, 0, 5], [3, 3, 1, 0], [2, 0, 0, 0]])

mask = np.array(
    [
        [3, 0, 1],
        [0, 1, 2],
        [2, 0, 1],
    ]
)

output_matrix = convolution(input_matrix, mask)

print(output_matrix)
