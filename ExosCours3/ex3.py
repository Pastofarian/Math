# 3.	Idem mais avec la fonction convolve de Scipy. Le résultat est-il identique ? Pourquoi ?

# Parce que Scipy utilise des tableaux multi-dimensions et ici il "flip" le mask automatiquement

from scipy.signal import convolve2d
import numpy as np


def convolution(input_matrix, mask):
    output = convolve2d(input_matrix, mask, mode="same")

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
