# Exercice 3 : éclaircir/assombrir une image
# Eclaircir une image (brighten) : Il suffit d’ajouter une valeur entière identique à chaque pixel en veillant à
# ce que le résultat ne dépasse pas 255. Pour assombrir, on retranche une valeur entière sans descendre
# en-dessous de zéro. Variante : retirer/ajouter une valeur différente pour chaque canal de couleur (on
# modifie dans ce cas la balance des couleurs. On peut aussi écrire en une ligne la modification en utilisant
# la fonction: np.where(condition,valeur_si_vraie,valeur_si_fausse) où la condition écrite sur un tableau
# de valeurs s'applique sur chaque valeur directement.
# Par exemple, np.where(t<30,0,t-30) permet de créer un tableau dans lequel toutes les valeurs de t
# inféreures strictement à 30 sont remplacée par 0 et celles au dessus de 30, on soustrait 30. Cela
# permettrait de réduire la luminosité de 30 si on l'applique à une image.

#!/usr/bin/env python
# -*- coding: utf8 -*-

# ----------------------------------------------------------#
#                                                          #
#               Project Math-Bac-Info-Python               #
#                     Template Python                      #
#                      G. Barmarin                         #
#                                                          #
# ----------------------------------------------------------#

# ----------------------------------------------------------#
#                Source: Gérard Barmarin                   #
# ----------------------------------------------------------#

# ----------------------------------------------------------#
#                Que fait ce programme?                    #
# ----------------------------------------------------------#

# Ce template vous permet de voir comment décomposer un tableau
# d'une image couleurs en 3 matrices séparées pour chaque canal
# de couleur pour pouvoir les traiter séparémment

# ----------------------------------------------------------#
#              Importation des librairies                  #
# ----------------------------------------------------------#

# Chargement des bibliothèques utilisées

import numpy as np  # bibliothèque mathématique
from PIL import Image, ImageTk  # on importe juste le module Image de PIL
import tkinter as tk

# -----------------------------------------------------------------------
# encodage des fonctions
# -----------------------------------------------------------------------


def quit_app():
    Mafenetre.destroy()


def brighten():
    global matrice_R1
    global matrice_G1
    global matrice_B1
    matrice_R1 = np.where(matrice_R > 204, 255, matrice_R + 50)
    matrice_G1 = np.where(matrice_G > 204, 255, matrice_G + 50)
    matrice_B1 = np.where(matrice_B > 204, 255, matrice_B + 50)
    mainLoop()


def darken():
    global matrice_R1
    global matrice_G1
    global matrice_B1
    matrice_R1 = np.where(matrice_R < 50, 0, matrice_R - 50)
    matrice_G1 = np.where(matrice_G < 50, 0, matrice_G - 50)
    matrice_B1 = np.where(matrice_B < 50, 0, matrice_B - 50)
    mainLoop()


def reset():
    global matrice_img_array_mod
    global matrice_R1, matrice_G1, matrice_B1
    matrice_img_array_mod = np.copy(matrice_img_array)
    matrice_R1 = matrice_img_array[:, :, 0]
    matrice_G1 = matrice_img_array[:, :, 1]
    matrice_B1 = matrice_img_array[:, :, 2]
    mainLoop()


def mainLoop():
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

brighten_button = tk.Button(button_frame, text="Brighten", command=brighten)
brighten_button.config(foreground="black")
brighten_button.pack(padx=(30, 30), pady=(15, 15))

darken_button = tk.Button(button_frame, text="Darken", command=darken)
darken_button.config(foreground="black")
darken_button.pack(padx=(45, 45), pady=(15, 15))

reset_button = tk.Button(button_frame, text="Reset", command=reset)
reset_button.config(foreground="black")
reset_button.pack(padx=(60, 60), pady=(15, 15))

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


# matrice_R = np.where(matrice_R < 50, +0, matrice_R - 50)
# matrice_G = np.where(matrice_G < 50, +0, matrice_G - 50)
# matrice_B = np.where(matrice_B < 50, +0, matrice_B - 50)

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
