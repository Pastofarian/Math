# Ecrivez un programme qui calcule les solutions d’un système d’équation.
# Le programme demandera combien il y a de variables et combien d'équations.
# Si les deux chiffres sont différents, affichage d'un message d'erreur (lequel?) et arrêt ou
# bouclage du programme pour reposer la question.
# Ensuite, boucle pour introduire le coefficient de chaque variable, équation par équation,
# mise en forme de la matrice correspondante et résolution du système (en utilisant pour
# l’inversion de matrice nécessaire le résultat de l’exercice précédent avec affichage du
# résultat

import numpy as np
from ex4 import (
    Gauss_Jordan_inverse,
)  # Importe la fonction de l'exercice 4 parce qu'on est fainéant


# Le programme demandera combien il y a de variables et combien d'équations.
def input_system():
    # Boucle jusqu'à ce que le nombre de variables soit égal au nombre d'équations
    while True:
        n_variables = int(input("Entrez le nombre de variables: "))
        n_equations = int(input("Entrez le nombre d'équations: "))

        if n_variables == n_equations:
            break
        else:
            print(
                "Erreur: Le nombre de variables doit être égal au nombre d'équations."
            )

    # Crée la matrice A et le vecteur b
    A = np.zeros((n_equations, n_variables))
    b = np.zeros(n_equations)

    # Rempli la matrice A et le vecteur b avec les valeurs entrées par l'utilisateur
    for i in range(n_equations):
        print(f"Entrez les coefficients pour l'équation {i + 1}:")
        for j in range(n_variables):
            A[i, j] = float(input(f"Coefficient pour la variable {j + 1}: "))
        b[i] = float(input("Entrez la valeur constante pour cette équation: "))

    return A, b


# Résout le système d'équations en utilisant l'inverse de la matrice A
def solve_system(A, b, Gauss_Jordan_inverse):
    A_inv = Gauss_Jordan_inverse(A)
    x = np.dot(A_inv, b)
    return x


# Mon main
if __name__ == "__main__":
    A, b = input_system()
    solutions = solve_system(A, b, Gauss_Jordan_inverse)
    print("Les solutions du système d'équations sont:")
    for i, s in enumerate(solutions, start=1):
        print(f"x{i} = {s}")
