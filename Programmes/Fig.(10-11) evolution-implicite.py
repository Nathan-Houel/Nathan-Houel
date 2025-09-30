import numpy as np
import matplotlib.pyplot as plt
from scipy import sparse
from scipy.sparse import linalg

# Paramètres de la simulation
lg = 10.        # intervalle en x=[-lg, lg]
nx = 60       # nombre de points du maillage
dx = (2*lg)/(nx-1)       # dx = pas d'espace
cfl = 0.4      # cfl = dt/dx^2, coefficient CFL
dt = dx*dx*cfl  # dt = pas de temps
Tfinal = 1.     # Temps final souhaité

print("Paramètres de la discrétisation : domaine (", -lg, lg, ") discretisé avec nx=", nx, " points de discrétisation et une taille de maille dx=", dx)

# Création du maillage en x
x = np.linspace(-lg, lg, nx)

# Initialisation de la condition initiale u0
u0 = np.zeros(len(x))
for k in range(len(x)):
    if abs(x[k]) < 1:
        u0[k] = 1
    else:
        u0[k] = 0

# Initialisation de u avec les données initiales u0
u = u0.copy()

# Construction de la matrice (creuse) pour le schéma implicite
Aimp = sparse.diags([-cfl, 1+2*cfl, -cfl], [-1, 0, 1], shape=(nx, nx), format='csc')
lu_Aimp = linalg.splu(Aimp, permc_spec='NATURAL')

# Nombre de pas de temps effectués
nt = int(Tfinal/dt)
Tfinal = nt*dt  # On corrige le temps final (si Tfinal/dt n'est pas entier)

# Boucle temporelle
for n in range(1, nt+1):
    u = lu_Aimp.solve(u)  # Résolution du système linéaire pour le schéma implicite

    # Affichage de la solution
    if n % 1 == 0:
        plt.plot(x, u, label='t = {:.2f}'.format(n*dt))

# Paramètres d'affichage final
plt.plot(x, u0, 'b', label='Condition initiale')
plt.xlabel('$x$')
plt.title('Schéma implicite - Évolution de la solution au fil du temps')
plt.legend()
plt.show()