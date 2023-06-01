# 10. Programmez un filtre de détection de contour basé sur le Laplacien avec ou sans pré-
# floutage

import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
from scipy.signal import convolve2d
from scipy.ndimage import gaussian_filter


# -----------------------------------------------------------------------
# encodage des fonctions
# -----------------------------------------------------------------------


def quit_app():
    Mafenetre.destroy()


def apply_laplacian_edge_detection_filter(image, pre_blur=False, sigma=1):
    image_array = np.asarray(image.convert("L"))  # converti en nuances de gris

    if pre_blur:
        image_array = gaussian_filter(image_array, sigma=sigma)

    laplacian = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

    laplacian_edges = convolve2d(image_array, laplacian, mode="same")
    laplacian_edges = np.clip(laplacian_edges, 0, 255).astype(np.uint8)

    return laplacian_edges


def on_laplacian_edge_detection_button_click(pre_blur=False):
    global matrice_img_array, photo2, canvas2

    # Applique le filtre de détection de contour Laplacien
    edge_detected_image = Image.fromarray(
        apply_laplacian_edge_detection_filter(mon_image, pre_blur=pre_blur)
    )

    # Update l'image modifiée du canvas
    matrice_img_array_mod = np.array(edge_detected_image)
    photo2 = ImageTk.PhotoImage(edge_detected_image)
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

laplacian_edge_detection_button = tk.Button(
    button_frame,
    text="Laplacian Detection",
    command=lambda: on_laplacian_edge_detection_button_click(False),
)
laplacian_edge_detection_button.pack(padx=(15, 15), pady=(15, 15))

pre_blurred_laplacian_edge_detection_button = tk.Button(
    button_frame,
    text="Pre-blurred",
    command=lambda: on_laplacian_edge_detection_button_click(True),
)
pre_blurred_laplacian_edge_detection_button.pack(padx=(15, 15), pady=(15, 15))


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
image_name = "Lenna512BW"
image_extension = "png"

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
