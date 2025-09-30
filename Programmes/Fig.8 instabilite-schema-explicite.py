import pylab
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy import sparse
from scipy.sparse import linalg

# Paramètres de la simulation
lg = 10.        # intervalle en x=[-lg, lg]
nx = 100        # nombre de points du maillage
dx = (2*lg)/(nx-1)       # dx = pas d'espace
cfl = 0.51      # cfl = dt/dx^2, coefficient CFL
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
u = u0.copy()  # Il faut faire une copie sinon on va changer u0 en changeant u

# Construction de la matrice (creuse) pour le schéma explicite
A = sp.sparse.diags([cfl, 1-2*cfl, cfl], [-1, 0, 1], shape=(nx-2, nx-2))

# Nombre de pas de temps effectués
nt = int(Tfinal/dt)
Tfinal = nt*dt  # On corrige le temps final (si Tfinal/dt n'est pas entier)

# Boucle temporelle
for n in range(1, nt+1):
    
    # Schéma explicite en temps
    u[1:len(u)-1] = A * u[1:len(u)-1]

    # Affichage de la solution
    if n % 5 == 0:
        plt.figure(1)
        plt.clf()
        plt.plot(x, u0, 'b', label='Condition initiale')
        plt.plot(x, u, 'r', label='Solution au temps $t=$ %s' % (n*dt))
        plt.xlabel('$x$')
        plt.title('Schéma explicite avec CFL=0.51, $t=$%s' % (n*dt))
        plt.legend()
        plt.pause(0.1)

# Affichage final
plt.figure(2)
plt.plot(x, u0, 'b', label='Condition initiale')
plt.plot(x, u, 'r', label='Solution finale au temps $t=$ %s' % Tfinal)
plt.xlabel('$x$')
plt.title('Solution finale avec CFL=0.51, $t=$%s' % Tfinal)
plt.legend()
plt.show()
