# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


def affichage(fonction, matrice):
    """Cette fonction nous permet d'afficher 10 itérations d'une matrice
    réparties sur 2 lignes et 5 colonnes.
    """
    tab = list()
    plt.subplots(2, 5)
    for i in range(10):
        matrice_bloc = fonction(matrice)
        tab.append(matrice_bloc)
        plt.imshow(tab[i])
        plt.title("Itération" + str(i+1))

    
def nb_alea(graine, matrice):
    """Cette fonction permet de créer une matrice composée de 1 et de 0
    avec une proportion de 1 égale à prop_active (dépendant de la graine).
    """
    prop_active = (1+graine)*10/100
    for i in range(1, np.shape(matrice)[0]-1):
        for j in range(1, np.shape(matrice)[1]-1):
            nombre_alea = np.random.binomial(n=1, p=float(prop_active))
            matrice[i, j] = nombre_alea
    return(matrice)