import pylab
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy import sparse
from scipy.sparse import linalg


lg = 10.        # intervalle en x=[-lg,lg]
nx = 100    # nombre de points du maillage
dx = (2*lg)/(nx-1)       # dx = pas d'espace
cfl = 0.4     # cfl = dt/dx^2
dt = dx*dx*cfl # dt = pas de temps
Tfinal = 1.   # Temps final souhaitÃ©

print("parametres de la discretisation : domaine (", -lg , lg , ") discretise avec nx=", nx, " points de discretisation et une taille de maille dx=", dx)

x = np.linspace(-lg,lg,nx)

# Initialize u0
u0 = np.zeros(len(x))
#print(len(u0))

# Set specific u0 values (same as in the scilab program)
for k in range (len(x)):
    if ( abs(x[k])<1) :
       u0[k] = 1
    else:
       u0[k] = 0


# Schemas numeriques

# Initialize u by the initial data u0
u = u0.copy() # il faut faire une copie sinon on va changer u0 en changeant u

# Construction de la matrice (creuse) pour le schema explicite
A = sp.sparse.diags([cfl, 1-2*cfl, cfl], [-1, 0, 1], shape=(nx-2, nx-2))

# Nombre de pas de temps effectues
nt = int(Tfinal/dt)
Tfinal = nt*dt # on corrige le temps final (si Tfinal/dt n'est pas entier)

# Création de la figure en dehors de la boucle
plt.figure(1)

# Boucle Temporelle
for n in range(1, nt+1):
    # Schema explicite en temps
    u[1:len(u)-1] = A*u[1:len(u)-1]

    # Print solution à chaque 5e itération
    if n % 5 == 0:
        plt.plot(x, u, label=f'Schema explicite, $t={n*dt}$')

# Ajouter des détails au graphique
plt.plot(x, u0, 'b', label='Donnée initiale')
plt.xlabel('$x$')
plt.title('Evolution de la solution (Schema explicite)')

# Ajouter la légende en dehors du graphique
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Afficher la figure finale
plt.show()