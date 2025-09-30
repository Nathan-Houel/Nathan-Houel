import numpy as np
import matplotlib.pyplot as plt
from scipy import sparse
from scipy.sparse import linalg

# Paramètres de la simulation
lg = 10.        # intervalle en x=[-lg, lg]
nx = 100        # nombre de points du maillage
dx = (2*lg)/(nx-1)       # dx = pas d'espace
cfl = 0.4       # cfl = dt/dx^2
dt = dx*dx*cfl  # dt = pas de temps
Tfinal = 1.     # Temps final souhaité

# Affichage des paramètres de la discrétisation
print("Paramètres de la discrétisation : domaine (", -lg, lg, ") discretisé avec nx=", nx, " points de discrétisation et une taille de maille dx=", dx)

# Création du maillage en x
x = np.linspace(-lg, lg, nx)

# Initialisation de la condition initiale u0 (une marche centrée)
u0 = np.zeros(len(x))
for k in range(len(x)):
    if abs(x[k]) < 1:
        u0[k] = 1
    else:
        u0[k] = 0

# Initialisation de la solution numérique u
u = u0.copy()

# Construction de la matrice (creuse) pour le schéma explicite
A = sparse.diags([cfl, 1-2*cfl, cfl], [-1, 0, 1], shape=(nx-2, nx-2))

# Nombre de pas de temps effectués
nt = int(Tfinal/dt)
Tfinal = nt*dt # on corrige le temps final (si Tfinal/dt n'est pas entier)

# Boucle temporelle pour le schéma explicite
for n in range(1, nt+1):
    # Mise à jour de la solution en utilisant le schéma explicite
    u[1:len(u)-1] = A * u[1:len(u)-1]

# Calcul de la solution exacte
uexacte = np.zeros(len(u0))
for i in range(int(nx)):
    for j in range(int(nx)-1):
        uexacte[i] = uexacte[i] + u0[j] * dx * noyauc((i-j)*dx, Tfinal)

# Comparaison entre solutions exacte et approchée au temps final
plt.figure(3)
plt.clf()
plt.suptitle("Comparaison entre solutions exacte et approchée au temps Tfinal")
plt.plot(x, u0, 'b', label='Donnée initiale')
plt.plot(x, u, 'or', label='Schema explicite CFL=0.4')
plt.plot(x, uexacte, 'k', label='Solution exacte')
plt.legend(loc='best')
plt.show()
