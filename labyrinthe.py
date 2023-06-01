##!/usr/bin/python
# -*- coding: utf8 -*-

# ----------------------------------------------------------------------#
#                                                                      #
#                 Cours de Mathématiques pour BAC Info                 #
#                            G. Barmarin                               #
#                                                                      #
#                          Exercice Graphes                            #
#                                                                      #
# ----------------------------------------------------------------------#

# ----------------------------------------------------------------------#
#                                                                      #
#                           Ex Labyrinthes                             #
#                                                                      #
# ----------------------------------------------------------------------#

# -----------------------------------------------------------------------
# Importation des bibliothèques
# -----------------------------------------------------------------------

import numpy as np  # bibliothèque mathématique
from pylab import *
import matplotlib  # bibliothèque d'affichage de courbes
import matplotlib.pyplot as plt
import random  # génération de nombre aléatoires

# -----------------------------------------------------------------------
# encodage des fonctions
# -----------------------------------------------------------------------


def voisins(p, M, N):
    # renvoie dans s les voisins de tous les sommets admissible de p
    s = [gauche(p), droit(p), bas(p), haut(p)]
    return [v for v in s if admissible(v, M, N)]


def gauche(p):
    # calcule les coordonnées du voisin de gauche
    x, y = p
    return (
        x - 1,
        y,
    )  # Le voisin de gauche a le même y (il est sur la même ligne), mais avec une abscisse valant 1 de moins!


def droit(p):
    x, y = p
    return (
        x + 1,
        y,
    )  # Le voisin de droite a le même y (il est sur la même ligne), mais avec une abscisse valant 1 de plus!


def bas(p):
    x, y = p
    return (
        x,
        y - 1,
    )  # Le voisin du bas a le même x (il est sur la même colonne, mais avec une ordonnée y valant 1 de moins!


def haut(p):
    x, y = p
    return (
        x,
        y + 1,
    )  # Le voisin du haut a le même x (il est sur la même colonne, mais avec une ordonnée y valant 1 de plus!


def admissible(v, M, N):
    # vérifie qu'un voisin existe (détection des bords)
    x, y = v
    return x >= 0 and x < M and y >= 0 and y < N


def creer_labyrinthe(p0, M, N):  # crée un labyrinthe de dimension MxN
    visites = set([p0])
    s = [p0]
    peres = {}
    while s != []:
        p = (
            s.pop()
        )  # list.pop(i) Enlève de la liste l'élément situé à la position indiquée et le renvoie en valeur de retour.
        vs = voisins(
            p, M, N
        )  # Si aucune position n'est spécifiée, a.pop() enlève et renvoie le dernier élément de la liste
        melanger(
            vs
        )  # la fonction melanger créée plus loin introduit le côté aléatoire pour créér des labyrinthes différents à chaque fois.
        for v in vs:
            if v not in visites:
                visites.add(v)
                s.append(v)
                peres[v] = p
    return peres


def melanger(s):
    # la fonction mélanger introduit le ôté aléatoire pour créér des labyrinthes différents à chaque fois.
    n = len(s)
    for k in range(n):
        j = random.randint(k, n - 1)
        s[j], s[k] = s[k], s[j]


def plot_arbre(t):
    # dessin de l'arbre en trait bleu au centre des cases du labyrinthe
    for a, b in t:
        c, d = t[(a, b)]
        plt.plot((a, c), (b, d), "b")
    plt.show()


def plot_labyrinthe(
    t,
    M,
    N,
    lab=False,  # passer en false pour avoir une vision plus claire (on retire le bleu)
):  # si lab=True, dessin de l'arbre dans le labyrinthe si lab=False non
    d = 0.5  # on trace le labyrinthe à une demi unité (0.5) du chemin de l'arbre complet
    plt.axis([-1, M, -1, N])
    for x in range(M + 1):
        plt.plot(
            (x - d, x - d), (-d, N - d), "k"
        )  # k = black dessin en noir du labyrinthe
    for y in range(N + 1):
        plt.plot((-d, M - d), (y - d, y - d), "k")
    for x, y in t:
        (a, b) = t[(x, y)]
        if a == x + 1:
            plt.plot(
                (x + d, x + d), (y - d, y + d), "w"
            )  # w=white suppression d'un côté en le dessinant en blanc sur blanc
        elif a == x - 1:
            plt.plot((x - d, x - d), (y - d, y + d), "w")
        elif b == y + 1:
            plt.plot((x - d, x + d), (y + d, y + d), "w")
        elif y == b + 1:
            plt.plot((x - d, x + d), (y - d, y - d), "w")
        if lab:
            plt.plot((x, a), (y, b), "b")
    # plt.show()


def peres_vers_graphe(peres):
    G = {}
    for x in peres:
        if x in G:
            G[x].append(peres[x])
        else:
            G[x] = [peres[x]]
        if peres[x] in G:
            G[peres[x]].append(x)
        else:
            G[peres[x]] = [x]
    return G


def nombre_sommets(G):
    return len(G)


def nombre_aretes(G):
    s = 0
    for p in G:
        s = s + len(G[p])
    return s


def explorer(G, p0):
    visites = set([p0])
    s = [p0]
    peres = {}
    while s != []:
        p = s.pop()
        vs = G[p]
        for v in vs:
            if v not in visites:
                visites.add(v)
                s.append(v)
                peres[v] = p
    return peres


def chemin(G, p, q):
    if p == q:
        return [p]
    else:
        peres = explorer(G, p)
        c = [q]
        while peres[q] != p:
            c.append(peres[q])
            q = peres[q]
        c.append(p)
        return c


def afficher_chemin(peres, M, N, chemin):
    plot_labyrinthe(peres, M, N)
    for k in range(len(chemin) - 1):
        (x, y) = chemin[k]
        (a, b) = chemin[k + 1]
        plt.plot(
            (x, a), (y, b), "r"
        )  # Affichage du chemin en surimpression rouge (r) sur l'arbre (s'il est affiché: lab=True)
    plt.show()


# -----------------------------------------------------------------------
# encodage du programme principal
# -----------------------------------------------------------------------

M = int(input("largeur du Labyrinthe? "))  # largeur du labyrinthe
# M=50
N = int(input("longueur du Labyrinthe? "))  # Longueur du labyrinthe
# N = 50
px = int(
    input("x du Point de départ? (< largeur) ")
)  # Introduction des coordonnées de départ et d'arrivée
py = int(input("y du Point de départ? (< longueur) "))
qx = int(input("x du Point d'arrivée? (< largeur) "))
qy = int(input("y du Point d'arrivée? (< longueur) "))

t = creer_labyrinthe((M // 2, N // 2), M, N)  # // = division entière
G = peres_vers_graphe(t)
p = (px, py)  # point de départ
q = (qx, qy)  # point d'arrivée
c = chemin(G, p, q)
c.reverse()
print(c)
afficher_chemin(t, M, N, c)
