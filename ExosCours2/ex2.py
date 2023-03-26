# Exercice 2 : isoler un canal de couleur
# Implémentez un bouton "Red" (ordinal=2) ou « Green » ou « blue ». Ce bouton éliminera toutes les
# couleurs de l'image, excepté le rouge (ou le vert ou le bleu). C'est assez simple : décomposez le tableau
# 512x512x3 en trois matrices 512x512x1, et assignez la valeur 0 aux 2 matrices dont vous ne voulez pas la
# couleur, en laissant inchangée la troisième. L’image résultante aura la couleur correspondante.
# Vous pouvez aussi recopier dans les trois matrices la valeur de la couleur qui vous intéresse. Dans ce cas
# l’mage finale sera en nuances de gris : plus le gris sera clair, plus la zone est rouge, plus elle est noire,
# moins il y a de rouge dans cette zone.
# Variante : utiliser un test de seuil et mettre à 0 la valeur du canal rouge si on atteint pas le seuil et à 255
# s’il est atteint, cela paermet d’afficher en rouge sur fond noir les zones où le seuil est atteint !
# (utilisez l’image du mandrill !)

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


def blue():
    global matrice_R
    global matrice_G
    matrice_R = 0
    matrice_G = 0
    mainLoop()


def red():
    global matrice_B
    global matrice_G
    matrice_B = 0
    matrice_G = 0
    mainLoop()


def green():
    global matrice_B
    global matrice_R
    matrice_B = 0
    matrice_R = 0
    mainLoop()


def reset():
    global matrice_img_array_mod
    global matrice_R, matrice_G, matrice_B
    matrice_img_array_mod = np.copy(matrice_img_array)
    matrice_R = matrice_img_array[:, :, 0]
    matrice_G = matrice_img_array[:, :, 1]
    matrice_B = matrice_img_array[:, :, 2]
    mainLoop()


def mainLoop():
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
quit_button.config(foreground="black")
quit_button.pack(padx=(15, 15), pady=(15, 15))

red_button = tk.Button(button_frame, text="Red", command=red)
red_button.config(foreground="red")
red_button.pack(padx=(30, 30), pady=(15, 15))

blue_button = tk.Button(button_frame, text="Blue", command=blue)
blue_button.config(foreground="blue")
blue_button.pack(padx=(45, 45), pady=(15, 15))

green_button = tk.Button(button_frame, text="Green", command=green)
green_button.config(foreground="green")
green_button.pack(padx=(60, 60), pady=(15, 15))

reset_button = tk.Button(button_frame, text="Reset", command=reset)
reset_button.config(foreground="black")
reset_button.pack(padx=(75, 75), pady=(15, 15))

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
image_name = "4-2-03"
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
