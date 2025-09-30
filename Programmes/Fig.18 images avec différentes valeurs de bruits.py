#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 11:01:50 2024

@author: maxencerobineau
"""

import numpy as np
from PIL import Image

def ajouter_bruit_gaussien(image, moyenne, ecart_type):
    """
    Ajoute du bruit gaussien à une image.

    :param image: Image d'entrée
    :param moyenne: Moyenne du bruit gaussien
    :param ecart_type: Écart-type du bruit gaussien
    :return: Image avec du bruit gaussien ajouté
    """
    bruit = np.random.normal(moyenne, ecart_type, image.shape)
    image_bruitee = image + bruit
    image_bruitee = np.clip(image_bruitee, 0, 255)  # Assurer que les valeurs restent dans la plage valide des valeurs d'une image en niveaux de gris
    return image_bruitee.astype(np.uint8)

chemin_image = "image2.jpeg"
image_originale = np.array(Image.open(chemin_image).convert('L'))  # Convertir en niveaux de gris

# Ajouter du bruit gaussien à l'image
image_bruitee = ajouter_bruit_gaussien(image_originale, moyenne=0, ecart_type=25)

# Enregistrer l'image bruitée
chemin_image_bruitee = "image_bruitee.jpeg"
Image.fromarray(image_bruitee).convert('L').save(chemin_image_bruitee)



