#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 13:00:26 2024

@author: maxencerobineau
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Fonction g pour la diffusion anisotrope de Perona et Malik
def g(x, K):
    return np.exp(-(x/K)**2)

# Fonction pour calculer la valeur K à partir du gradient de l'image
def valeur_K(image):
    images = image.astype(float)
    gradient_x, gradient_y = np.gradient(images)
    gradient = np.append(abs(gradient_x), abs(gradient_y))
    
    # Tri de la liste des gradients
    gradient_trie = np.sort(gradient)
    print("K=",gradient_trie[int(len(gradient) * 0.95)])
    # Retourne la valeur qui est 90 % plus grande dans le gradient trié
    return gradient_trie[int(len(gradient) * 0.95)]

# Fonction pour appliquer la diffusion anisotrope de Perona et Malik
def perona_malik(image, num_iterations, delta_t, K):
    images = image.astype(float)
    
    for _ in range(num_iterations):
        updated_image = images.copy()

        for x in range(1, len(updated_image) - 1):
            for y in range(1, len(updated_image[0]) - 1):
                term1 = g(np.abs(updated_image[x - 1, y] - updated_image[x, y]), K) * (updated_image[x - 1, y] - updated_image[x, y])
                term2 = g(np.abs(updated_image[x + 1, y] - updated_image[x, y]), K) * (updated_image[x + 1, y] - updated_image[x, y])
                term3 = g(np.abs(updated_image[x, y - 1] - updated_image[x, y]), K) * (updated_image[x, y - 1] - updated_image[x, y])
                term4 = g(np.abs(updated_image[x, y + 1] - updated_image[x, y]), K) * (updated_image[x, y + 1] - updated_image[x, y])

                # Ajouter les termes à une image temporaire
                updated_image[x, y] = updated_image[x, y] + delta_t * (term1 + term2 + term3 + term4)

        # Mettre à jour l'image après la fin de chaque itération
        images = updated_image

    return updated_image.astype(np.uint8)

# Charger une image à partir d'un dossier
image_path = "image_bruitee.jpeg"
image="image.jpeg"
image_bruitee = np.array(Image.open(image_path).convert('L'))  # Convertir en niveaux de gris
image_original = np.array(Image.open(image).convert('L'))

# Appliquer le filtrage Perona et Malik
image_filtree = perona_malik(image_bruitee, num_iterations=200, delta_t=0.2, K=valeur_K(image_bruitee))


# Fonction pour afficher les images
def display_images(original, bruitee,filtre):
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
    plt.title('Filtre Perona et Malik')
    plt.axis('off')
 
    plt.show()
    
# Afficher les images
display_images(image_original,image_bruitee, image_filtree)

