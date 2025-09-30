#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 13:28:46 2024

@author: maxencerobineau
"""
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Fonction pour créer un noyau gaussien
def noyau_gaussien(taille_noyau, sigma):
    ax = np.linspace(-(taille_noyau - 1) / 2., (taille_noyau - 1) / 2., taille_noyau)
    x, y = np.meshgrid(ax, ax)
    noyau = np.exp(-(x**2 + y**2) / (2. * sigma**2))
    noyau /= 2 * np.pi * sigma**2
    return noyau

# Fonction pour appliquer un filtre gaussien à une image
def filtre_gaussien(image, taille_noyau=51, sigma=5):
    noyau = noyau_gaussien(taille_noyau, sigma)
    demi_noyau = taille_noyau // 2
    image_remplie = np.pad(image, ((demi_noyau, demi_noyau), (demi_noyau, demi_noyau)), mode='edge')
    image_filtree = np.zeros_like(image, dtype=float)

    for i in range(demi_noyau, image_remplie.shape[0] - demi_noyau):
        for j in range(demi_noyau, image_remplie.shape[1] - demi_noyau):
            region = image_remplie[i - demi_noyau:i + demi_noyau + 1, j - demi_noyau:j + demi_noyau + 1]
            image_filtree[i - demi_noyau, j - demi_noyau] = np.sum(region * noyau)

    # Ajuster la plage des valeurs pour éviter l'assombrissement excessif
    image_filtree = (image_filtree / np.max(image_filtree)) * 255

    return image_filtree.astype(np.uint8)

# Charger l'image bruitée
image_path_bruitee = "image_bruitee.jpeg"
image_bruitee = np.array(Image.open(image_path_bruitee).convert('L'))
chemin_image = "image.jpeg"
image_originale = np.array(Image.open(chemin_image).convert('L'))  # Convertir en niveaux de gris

# Appliquer le filtrage gaussien
image_filtree = filtre_gaussien(image_bruitee)

# Fonction pour afficher les images
def display_images(original, bruitee, filtre):
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(original, cmap='gray', vmin=0, vmax=255)
    plt.title('Image originale')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(bruitee, cmap='gray', vmin=0, vmax=255)
    plt.title('Image bruitée')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(filtre, cmap='gray', vmin=0, vmax=255)
    plt.title('Filtre Gaussien')
    plt.axis('off')
    
    plt.show()

# Afficher les images
display_images(image_originale, image_bruitee, image_filtree)