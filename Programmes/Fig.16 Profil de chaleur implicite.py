import numpy as np
import matplotlib.pyplot as plt
import time

#Paramètres
L = 12.0  #Domaine selon x et y
alpha = 0.5  #Coefficient de diffusion
Nx, Ny = 100, 100  #Nombre de points en x et y
Nt = 500  #Nombre de points pour le temps

debut = time.time()

#Fonction f définissant les conditions initiales
def initial_condition(x, y):
    return np.where(np.logical_and(np.abs(x) <= 1, np.abs(y) <= 1), 1.0, 0.0)

#Calcul des pas de discrétisation
dx = L / (Nx - 1)
dy = L / (Ny - 1)
dt = 1 / Nt

#Mise en place d'une grille selon x et y
x = np.linspace(-L/2, L/2, Nx)
y = np.linspace(-L/2, L/2, Ny)
X, Y = np.meshgrid(x, y)
u = initial_condition(X, Y)

#Création de la liste avec les valeurs voulues pour t
time = [0.1, 0.5, 1.0, 3.0]

#Calcul de la solution grâce au schéma implicite + affichage pour les différentes valeurs de t
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
for i, t in enumerate(time):
    for n in range(int(Nt * t)):
        u[1:-1, 1:-1] += alpha * dt / dx**2 * (u[2:, 1:-1] - 2*u[1:-1, 1:-1] + u[:-2, 1:-1])
        u[1:-1, 1:-1] += alpha * dt / dy**2 * (u[1:-1, 2:] - 2*u[1:-1, 1:-1] + u[1:-1, :-2])
        
    ax = axes[i // 2, i % 2]
    im = ax.imshow(u, extent=[-L/2, L/2, -L/2, L/2], origin='lower', cmap='hot', aspect='auto', interpolation='bilinear')
    ax.set_title(f'Profil de chaleur à t={t}')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    

temps = time.time() - debut
print(f"Le programme a mis {temps} secondes")
plt.tight_layout()
plt.show()

