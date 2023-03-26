# Exercice 6 : transformer une image couleurs en tons sépia
# Implémentez un bouton "Sepia" pour convertir une image couleur en nuances de sépia.
# En photographie, le sépia est une qualité de tirage qui ressemble au noir et blanc, mais avec des
# variations de brun, et non de gris. La couleur sépia dans le système RVB est S(94, 38, 18).
# Le ton sépia rappelle l'aspect visuel des photographies du début du XXe siècle. Cet effet peut être
# obtenu grâce à l'application linéaire dont la matrice figure ci-dessous :
# Dans la mesure où la somme des coefficients d'une même ligne est supérieure à 1, le résultat de la
# combinaison linéaire doit être limité à 255 si celui-ci est hors de l'intervalle [0,255].


#!/usr/bin/env python
# -*- coding: utf8 -*-


# Chargement des bibliothèques utilisées

import numpy as np  # bibliothèque mathématique
from PIL import Image, ImageTk  # on importe juste le module Image de PIL
import tkinter as tk

# -----------------------------------------------------------------------
# encodage des fonctions
# -----------------------------------------------------------------------


def quit_app():
    Mafenetre.destroy()


def sepia_filter(matrice_R, matrice_G, matrice_B):
    sepia_R = np.clip(0.393 * matrice_R + 0.769 * matrice_G + 0.189 * matrice_B, 0, 255)
    sepia_G = np.clip(0.349 * matrice_R + 0.686 * matrice_G + 0.168 * matrice_B, 0, 255)
    sepia_B = np.clip(0.272 * matrice_R + 0.534 * matrice_G + 0.131 * matrice_B, 0, 255)
    # np.clip limite les valeurs d'un tableau.
    # On limite les valeurs de chaque couleur entre 0 et 255 ici.

    mainLoop(sepia_R, sepia_G, sepia_B)


def mainLoop(matrice_R1, matrice_G1, matrice_B1):
    matrice_img_array_mod[:, :, 0] = matrice_R1
    matrice_img_array_mod[:, :, 1] = matrice_G1
    matrice_img_array_mod[:, :, 2] = matrice_B1

    # Affichage de l'image modifiée dans le canevas de droite

    mon_image_mod = Image.fromarray(
        matrice_img_array_mod
    )  # Transformation du tableau de l'image modifiée en image PIL
    photo2 = ImageTk.PhotoImage(
        mon_image_mod
    )  # préparation de l'image pour affichage dans tk
    canvas2.create_image(
        0, 0, anchor=tk.NW, image=photo2
    )  # placement de l'image dans canvas2
    canvas2.pack()  # mise à jour de l'affichage du canvas2

    # Sauvetage de l'image modifiée dans le répertoire des images modifiées

    mon_image_mod.save(
        image_mod_directory + "/" + image_name + "_mod." + image_extension
    )  # Enregistrement d'une image contenue dans imgpil si le format n'est pas précisé, pil le choisit en accord avec l'extension du fichier

    # ----------------------------------------------------------#
    #            Boucle d'affichage dans tkinter               #
    # ----------------------------------------------------------#

    Mafenetre.mainloop()


# ----------------------------------------------------------#
#         Préparation de l'environnement tkinter           #
# ----------------------------------------------------------#

# Creation de la fenetre principale
Mafenetre = tk.Tk()  # Nom de la fenetre
Mafenetre.geometry(
    "1240x550+150+100"
)  # definit la taille de la fenetre (680x480) et sa position initiale (150 du bord gauche et 50 du bord supérieur)
Mafenetre.resizable(width=False, height=False)  # pour empêcher le redimensionnement
Mafenetre.title("Template du cours de Math")
Mafenetre["bg"] = "silver"  # couleur de fond de la fenetre bisque ou #FFFF00 pour jaune

# Creation du frame pour les boutons
button_frame = tk.Frame(Mafenetre, width=40, height=512, bd=8)
button_frame.pack(side="right", padx=(15, 15))
# Creation des boutons
quit_button = tk.Button(button_frame, text="Quitter", command=quit_app)
quit_button.config(foreground="red")
quit_button.pack(padx=(15, 15), pady=(15, 15))

sepia_button = tk.Button(
    button_frame,
    text="Sepia",
    command=lambda: sepia_filter(matrice_R, matrice_G, matrice_B),
)  # Fonction lambda : petite fonction anonyme avec plusieurs arguments mais une seule expression.
sepia_button.config(foreground="black")
sepia_button.pack(padx=(30, 30), pady=(15, 15))

# Creation du frame pour les images
images_frame = tk.Frame(Mafenetre, width=1100, height=400, bg="grey100")
images_frame.pack(side="left", padx=(15, 15), pady=(15, 15))
label1 = tk.Label(images_frame, text="Avant			              		Après", bg="grey100")
label1.pack(side="top")
# Creation du Canvas pour l'image originale
canvas1 = tk.Canvas(
    images_frame, width=512, height=512, bg="#00ffff", bd=-2
)  # bd= -2 supprime le bord du canevas
canvas1.pack(side="left", padx=(15, 5), pady=(15, 15))
# Creation du Canvas pour l'image traitée
canvas2 = tk.Canvas(
    images_frame, width=512, height=512, bg="#ff00ff", bd=-2
)  # bd= -2 supprime le bord du canevas
canvas2.pack(side="left", padx=(5, 15), pady=(15, 15))


# -----------------------------------------------------------------------
# encodage du programme principal
# -----------------------------------------------------------------------

print("\n---------------------------------------------\n")

# Ouverture de l'image et mise dans une matrice/tableau numpy

print(
    "\nOuverture avec numpy de l'image Lenna512.jpg se trouvant dans le répertoire images/ \n et stockage dans un tableau numpy\n"
)
image_directory = "images"  # les répertoires doivent exister
image_mod_directory = "images_mod"  # les répertoires doivent exister
image_name = "Lenna512"
image_extension = "jpg"

# Ouverture de l'image avec le module Image de PIL et placement dans un tableau
mon_image = Image.open(image_directory + "/" + image_name + "." + image_extension)
matrice_img_array = np.array(mon_image)

# Affichage de l'image originale dans le canevas de gauche de tkinter

photo = ImageTk.PhotoImage(
    mon_image
)  # creation d une image compatible Tkinter que vous pourrez afficher dans un Canvas par la méthode create_image(position, **options)
canvas1.create_image(0, 0, anchor=tk.NW, image=photo)
canvas1.pack()


# dont on peut demander les caractéristiques
print("classe :", type(matrice_img_array))
print("type :", matrice_img_array.dtype)
print("taille :", matrice_img_array.shape)

# Accès aux valeurs RGB d'un pixel de coordonnées (3,511) et affichage
print("Valeur RGB du pixel (3,511): ", matrice_img_array[250, 250, :])

# Affichage partiel de la matrice
print(
    "\nmatrix_img correspondant à l'image Lenna512.jpg: \n\n", matrice_img_array, "\n"
)

print("\n---------------------------------------------\n")

# Copie du tableau de l'image originale dans un nouveau tableau
matrice_img_array_mod = np.copy(matrice_img_array)

# Extraction des couches Rouge Vert Bleu
matrice_R = matrice_img_array[
    :, :, 0
]  # Extraction de la couche Rouge dans une matrice nxp à 2 dimensions
matrice_G = matrice_img_array[
    :, :, 1
]  # Extraction de la couche Vertee dans une matrice nxp à 2 dimensions
matrice_B = matrice_img_array[
    :, :, 2
]  # Extraction de la couche Bleue dans une matrice nxp à 2 dimensions

# Exemple de traitement des couches:
# on ne garde que la couche bleue qu'on recopie sur les deux autres canaux

# matrice_R = matrice_B
# matrice_G = matrice_B
# matrice_B = matrice_B

# Reconstitution du tableau correspondant à la nouvelle image RGB

matrice_img_array_mod[:, :, 0] = matrice_R
matrice_img_array_mod[:, :, 1] = matrice_G
matrice_img_array_mod[:, :, 2] = matrice_B

# Affichage de l'image modifiée dans le canevas de droite

mon_image_mod = Image.fromarray(
    matrice_img_array_mod
)  # Transformation du tableau de l'image modifiée en image PIL
photo2 = ImageTk.PhotoImage(
    mon_image_mod
)  # préparation de l'image pour affichage dans tk
canvas2.create_image(
    0, 0, anchor=tk.NW, image=photo2
)  # placement de l'image dans canvas2
canvas2.pack()  # mise à jour de l'affichage du canvas2

# Sauvetage de l'image modifiée dans le répertoire des images modifiées

mon_image_mod.save(
    image_mod_directory + "/" + image_name + "_mod." + image_extension
)  # Enregistrement d'une image contenue dans imgpil si le format n'est pas précisé, pil le choisit en accord avec l'extension du fichier

# ----------------------------------------------------------#
#            Boucle d'affichage dans tkinter               #
# ----------------------------------------------------------#

Mafenetre.mainloop()
