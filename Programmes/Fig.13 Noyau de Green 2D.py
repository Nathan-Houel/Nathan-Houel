import numpy as np
import matplotlib.pyplot as plt

# Fonction W
def W(x, y, t):
    return 1/(2*np.pi*t) * np.exp(-(x**2 + y**2)/(2*t))

# Création des différentes valeurs de x et y
x = np.linspace(-5, 5, 150)
y = np.linspace(-5, 5, 150)
t = 1.0

# Mise en place d'une grille 2D
X, Y = np.meshgrid(x, y)
Z = W(X, Y, t)  # Calcul de W pour chaque paire X,Y

# Affichage
plt.imshow(Z, extent=[-5, 5, -5, 5], cmap='hot', origin='lower', aspect='auto')
plt.colorbar(label='W(x, y, t)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Noyau de Green 2D pour t={}'.format(t))
plt.show()
