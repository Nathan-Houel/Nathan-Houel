import numpy as np
import matplotlib.pyplot as plt
import time

#Paramètres
alpha = 0.5
Lx, Ly = 10, 10  #Domaine de x et y
Nx, Ny = 100, 100  #Nombres de points en x et y
Nt = 500  #Nombres de points pour le temps

debut = time.time()

#Fonction f définissant les conditions initiales
def f(x, y):
    return 1.0 if -1 <= x <= 1 and -1 <= y <= 1 else 0.0

#Calcul des pas de discrétisation
dx = Lx / (Nx - 1)
dy = Ly / (Ny - 1)
dt = 1 / Nt

#Mise en place des conditions initiales
u = np.zeros((Nx, Ny))
for i in range(Nx):
    for j in range(Ny):
        u[i, j] = f(i * dx - Lx / 2, j * dy - Ly / 2)

#Liste des différentes valeurs de t voulues
temps = [0.1, 0.5, 1.0, 3.0]

#Calcul de la solution par la méthode des différences finies explicites + affichage des graphes pour chaque t
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
for k, t in enumerate(temps):
    for _ in range(int(Nt * t / t)):
        unew = u.copy()
        for i in range(1, Nx - 1):
            for j in range(1, Ny - 1):
                uxx = (u[i + 1, j] - 2 * u[i, j] + u[i - 1, j]) / dx**2
                uyy = (u[i, j + 1] - 2 * u[i, j] + u[i, j - 1]) / dy**2
                unew[i, j] = u[i, j] + alpha * dt * (uxx + uyy)
        u = unew

    axs[k // 2, k % 2].imshow(u, extent=[0, Lx, 0, Ly], cmap='hot', origin='lower', aspect='auto')
    axs[k // 2, k % 2].set_title(f'Profil de chaleur à t = {t}')
    axs[k // 2, k % 2].set_xlabel('X')
    axs[k // 2, k % 2].set_ylabel('y')
plt.tight_layout()
plt.show()

fin = time.time()
temps = fin - debut
print(f"Le programme a mis {temps} secondes")


