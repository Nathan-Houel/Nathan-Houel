#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 14:15:23 2024

@author: maxencerobineau
"""

from PIL import Image
import numpy as np

# Créer une image avec la moitié gauche en gris et la moitié droite en blanc
largeur, hauteur = 400, 200
image = np.zeros((hauteur, largeur), dtype=np.uint8)
image[:, :largeur//2] = 128  # Moitié gauche en gris (valeur 128)
image[:, largeur//2:] = 255  # Moitié droite en blanc (valeur 255)

# Enregistrer l'image sous le nom "image.png"
chemin_image = "image.jpeg"
Image.fromarray(image).convert('L').save(chemin_image)

# Afficher l'image
Image.fromarray(image).show()