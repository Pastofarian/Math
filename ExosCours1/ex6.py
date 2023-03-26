# Exercice 6
# En Python, créer un programme qui exécute le produit de deux matrices. Les matrices sont entrées au clavier élément par élément. Leur compatibilité est vérifiée avant d’introduire tous les éléments. Les matrices de départ et le produit sont affichés à l’écran.

# Demander la taille des matrices à l'utilisateur
n1 = int(input("Entrez le nombre de lignes de la première matrice : "))
m1 = int(input("Entrez le nombre de colonnes de la première matrice : "))
n2 = int(input("Entrez le nombre de lignes de la deuxième matrice : "))
m2 = int(input("Entrez le nombre de colonnes de la deuxième matrice : "))

# Vérifier si les matrices sont compatibles pour le produit
if m1 != n2:
    print("Les matrices ne sont pas compatibles pour le produit.")
else:
    # Initialiser les matrices
    matrice1 = []
    matrice2 = []
    produit = []

    # Demander à l'utilisateur de saisir les éléments des matrices
    print("Saisissez les éléments de la première matrice :")
    for i in range(n1):
        ligne = []
        for j in range(m1):
            element = float(input("Entrez l'élément ({}, {}) : ".format(i + 1, j + 1)))
            ligne.append(element)
        matrice1.append(ligne)

    print("Saisissez les éléments de la deuxième matrice :")
    for i in range(n2):
        ligne = []
        for j in range(m2):
            element = float(input("Entrez l'élément ({}, {}) : ".format(i + 1, j + 1)))
            ligne.append(element)
        matrice2.append(ligne)

    # Effectuer le produit des deux matrices
    for i in range(n1):
        ligne = []
        for j in range(m2):
            element = 0
            for k in range(m1):
                element += matrice1[i][k] * matrice2[k][j]
            ligne.append(element)
        produit.append(ligne)

    # Afficher les matrices et leur produit
    print("Matrice 1 :")
    for ligne in matrice1:
        print(ligne)
    print("Matrice 2 :")
    for ligne in matrice2:
        print(ligne)
    print("Produit des deux matrices :")
    for ligne in produit:
        print(ligne)
