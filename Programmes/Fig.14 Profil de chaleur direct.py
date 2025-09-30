import numpy as np
import matplotlib.pyplot as plt

#Fonction f qui définit les conditions initiales
def f(x, y):
    return np.where((np.abs(x) <= 1) & (np.abs(y) <= 1), 1.0, 0.0)

#Fonction u qui retourne le résultat de la convolution entre f et W
def u(x, y, t):
    return np.exp(-t) * f(x, y) + (1 - np.exp(-t)) * np.exp(-(x**2 + y**2) / (2 * t)) / (2 * np.pi * t)

#Différentes valeurs de temps choisies 
t_values = [0.1, 0.5, 1.5, 3.0]

#Création d'une grille d'abscisse x et d'ordonnées y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

#Affiche le profil de chaleur 2D pour chaque valeur de t 
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
for t, ax in zip(t_values, axes.flatten()):
    Z = u(X, Y, t)
    contour = ax.contourf(X, Y, Z, cmap='hot', levels=100)
    ax.set_title('Profil de chaleur à t={}'.format(t))
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.colorbar(contour, ax=ax)
plt.tight_layout()
plt.show()
