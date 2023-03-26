# Exercice 17 : Redimensionner une image
# Supposons que nous voulions redimensionner notre image qui est de dimension a0 lignes et b0 colonnes
# en une nouvelle dimension a1 lignes et b1 colonnes.
# On peut noter alors les ratios des transformations selon les lignes et les colonnes :
# ratio_lignes = a0/a1 et ratio_colonnes = b0/b1.
# Pour remplir notre nouvelle image, il suffit alors de remplir le pixel situé à la ligne ligne et la colonne col
# avec les couleurs du pixel de l'image de départ situé à la ligne int(ligne*ratio_lignes) et la colonne
# int(col*ratio_colonnes).
# Remarque : Si on fait ainsi, lors d'un agrandissement, plusieurs pixels de l'image de départ seront
# recopiés donnant une impression de gros pixels. Il existe beaucoup de façon d'empêcher ce phénomène
# en lissant les couleurs par différentes méthodes mais nous ne nous y intéresserons pas ici.
# Ecrivez un programme qui affiche une image en sortie de dimension 220 lignes et 220 colonnes de Lenna
# à partir de celle de 512x512.

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


def resize_image(matrice_R, matrice_G, matrice_B, new_rows, new_cols):
    a0, b0 = matrice_R.shape
    a1, b1 = new_rows, new_cols
    ratio_lignes = a0 / a1
    ratio_colonnes = b0 / b1

    resized_shape = (a1, b1, 3)
    resized_img_array = np.zeros(resized_shape, dtype=np.uint8)

    for row in range(a1):
        for col in range(b1):
            src_row = int(row * ratio_lignes)
            src_col = int(col * ratio_colonnes)
            resized_img_array[row, col, 0] = matrice_R[src_row, src_col]
            resized_img_array[row, col, 1] = matrice_G[src_row, src_col]
            resized_img_array[row, col, 2] = matrice_B[src_row, src_col]

    return resized_img_array


# Creation de la fenetre principale
Mafenetre = tk.Tk()
Mafenetre.geometry("1240x550+150+100")
Mafenetre.resizable(width=False, height=False)
Mafenetre.title("Redimensionnement d'image")
Mafenetre["bg"] = "silver"

button_frame = tk.Frame(Mafenetre, width=40, height=512, bd=8)
button_frame.pack(side="right", padx=(15, 15))

quit_button = tk.Button(button_frame, text="Quitter", command=quit_app)
quit_button.config(foreground="red")
quit_button.pack(padx=(15, 15), pady=(15, 15))

images_frame = tk.Frame(Mafenetre, width=1100, height=400, bg="grey100")
images_frame.pack(side="left", padx=(15, 15), pady=(15, 15))

label1 = tk.Label(images_frame, text="Avant			              		Après", bg="grey100")
label1.pack(side="top")

canvas1 = tk.Canvas(images_frame, width=512, height=512, bg="#00ffff", bd=-2)
canvas1.pack(side="left", padx=(15, 5), pady=(15, 15))

canvas2 = tk.Canvas(images_frame, width=512, height=512, bg="#ff00ff", bd=-2)
canvas2.pack(side="left", padx=(5, 15), pady=(15, 15))

image_directory = "images"
image_mod_directory = "images_mod"
image_name = "Lenna512"
image_extension = "jpg"

mon_image = Image.open(image_directory + "/" + image_name + "." + image_extension)
matrice_img_array = np.array(mon_image)

photo = ImageTk.PhotoImage(mon_image)
canvas1.create_image(0, 0, anchor=tk.NW, image=photo)
canvas1.pack()

matrice_R = matrice_img_array[:, :, 0]
matrice_G = matrice_img_array[:, :, 1]
matrice_B = matrice_img_array[:, :, 2]

# Resize the image
resized_image = resize_image(matrice_R, matrice_G, matrice_B, 220, 220)

# Create a PIL Image from the resized image array
mon_image_mod = Image.fromarray(resized_image)

# Save the resized image
mon_image_mod.save("images_mod/Lenna512_resized.jpg")
