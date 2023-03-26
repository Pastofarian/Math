# Exercice 10
# En Python, créer un programme qui exécute le produit de Hadamard de deux matrices. Les matrices sont entrées au clavier élément par élément. Leur compatibilité est vérifiée avant d’introduire tous les éléments. Les matrices de départ et le produit sont affichés à l’écran.

# Définir la taille de la première matrice
n1 = int(input("Entrez le nombre de lignes de la première matrice : "))
m1 = int(input("Entrez le nombre de colonnes de la première matrice : "))

# Définir la taille de la deuxième matrice
n2 = int(input("Entrez le nombre de lignes de la deuxième matrice : "))
m2 = int(input("Entrez le nombre de colonnes de la deuxième matrice : "))

# Vérifier la compatibilité des matrices
if n1 != n2 or m1 != m2:
    print("Erreur : les matrices ne sont pas de même dimension.")
else:
    # Créer la première matrice
    matrice1 = []
    for i in range(n1):
        ligne = []
        for j in range(m1):
            element = int(
                input(f"Entrez l'élément ({i+1}, {j+1}) de la première matrice : ")
            )
            ligne.append(element)
        matrice1.append(ligne)

    # Créer la deuxième matrice
    matrice2 = []
    for i in range(n2):
        ligne = []
        for j in range(m2):
            element = int(
                input(f"Entrez l'élément ({i+1}, {j+1}) de la deuxième matrice : ")
            )
            ligne.append(element)
        matrice2.append(ligne)

    # Calculer le produit de Hadamard
    produit = []
    for i in range(n1):
        ligne = []
        for j in range(m1):
            element = matrice1[i][j] * matrice2[i][j]
            ligne.append(element)
        produit.append(ligne)

    # Afficher les matrices et le produit de Hadamard
    print("Matrice 1 :")
    for ligne in matrice1:
        print(ligne)

    print("Matrice 2 :")
    for ligne in matrice2:
        print(ligne)

    print("Produit de Hadamard :")
    for ligne in produit:
        print(ligne)
