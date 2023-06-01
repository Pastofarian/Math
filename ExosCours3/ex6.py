# 6. Imaginez le masque d’un filtre de flou directionnel de gauche à droite (comme si la
# personne ne bougeait que dans cette direction) et testez-le


import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
from scipy.signal import convolve2d


# -----------------------------------------------------------------------
# encodage des fonctions
# -----------------------------------------------------------------------


def quit_app():
    Mafenetre.destroy()


def apply_motion_blur_filter(image, filter_size):
    image_array = np.asarray(image)
    blur_filter = np.zeros((filter_size, filter_size))
    np.fill_diagonal(blur_filter, 1 / filter_size)
    result = []

    for channel in range(3):  # A modifier si en noir et blanc
        result.append(convolve2d(image_array[:, :, channel], blur_filter, mode="same"))

    return np.stack(result, axis=-1).astype(np.uint8)


def on_motion_blur_button_click(filter_size):
    global matrice_img_array, photo2, canvas2

    # Applique le filtre de flou directionnel
    blurred_image = Image.fromarray(apply_motion_blur_filter(mon_image, filter_size))

    # Update l'image modifiée du canvas
    matrice_img_array_mod = np.array(blurred_image)
    photo2 = ImageTk.PhotoImage(blurred_image)
    canvas2.create_image(0, 0, anchor=tk.NW, image=photo2)
    canvas2.pack()


# Creation de la fenetre principale
Mafenetre = tk.Tk()
Mafenetre.geometry("1240x550+150+100")
Mafenetre.resizable(width=False, height=False)
Mafenetre.title("Template du cours de Math")
Mafenetre["bg"] = "silver"

# Création des cadres et des boutons
button_frame = tk.Frame(Mafenetre, width=40, height=512, bd=8)
button_frame.pack(side="right", padx=(15, 15))

quit_button = tk.Button(button_frame, text="Quitter", command=quit_app)
quit_button.config(foreground="red")
quit_button.pack(padx=(15, 15), pady=(15, 15))

motion_blur_button = tk.Button(
    button_frame,
    text="Motion Blur",
    command=lambda: on_motion_blur_button_click(
        15
    ),  # On peut contrôler la puissance du filtre (15)
)
motion_blur_button.pack(padx=(15, 15), pady=(15, 15))

images_frame = tk.Frame(Mafenetre, width=1100, height=400, bg="grey100")
images_frame.pack(side="left", padx=(15, 15), pady=(15, 15))

label1 = tk.Label(images_frame, text="Avant			              		Après", bg="grey100")
label1.pack(side="top")

# Création des Canvas pour afficher les images
canvas1 = tk.Canvas(images_frame, width=512, height=512, bg="#00ffff", bd=-2)
canvas1.pack(side="left", padx=(15, 5), pady=(15, 15))

canvas2 = tk.Canvas(images_frame, width=512, height=512, bg="white", bd=-2)
canvas2.pack(side="left", padx=(5, 15), pady=(15, 15))

# Chargement de l'image
image_directory = "images"
image_mod_directory = "images_mod"
image_name = "Lenna512"
image_extension = "jpg"

mon_image = Image.open(image_directory + "/" + image_name + "." + image_extension)
matrice_img_array = np.array(mon_image)

# Affichage de l'image originale
photo = ImageTk.PhotoImage(mon_image)
canvas1.create_image(0, 0, anchor=tk.NW, image=photo)
canvas1.pack()

matrice_R = matrice_img_array[:, :, 0]
matrice_G = matrice_img_array[:, :, 1]
matrice_B = matrice_img_array[:, :, 2]

Mafenetre.mainloop()
