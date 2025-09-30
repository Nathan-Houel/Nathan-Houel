import numpy as np
import matplotlib.pyplot as plt

lg = 10.        # intervalle en x=[-lg,lg]
nx = 100        # nombre de points du maillage
dx = (2*lg)/(nx-1)       # dx = pas d'espace
cfl = 0.4       # cfl = dt/dx^2
dt = dx*dx*cfl  # dt = pas de temps
Tfinal = 1.     # Temps final souhaité

x = np.linspace(-lg, lg, nx)

# Initialize u0
u0 = np.zeros(len(x))

# Set specific u0 values (same as in the scilab program)
for k in range(len(x)):
    if abs(x[k]) < 1:
        u0[k] = 1
    else:
        u0[k] = 0

# Import NumPy before using its functions
import numpy as np

# Initialize uexacte
uexacte = np.zeros(100)

# Define the noyauc function
def noyauc(x, t):
    return np.exp(-x**2 / (4*t)) / np.sqrt(4*np.pi*t)

# Calculate uexacte using the noyauc function
for i in range(int(nx)):
    for j in range(int(nx)-1):
        uexacte[i] = uexacte[i] + u0[j] * dt * noyauc((i-j)*dx, 0.1)

# Plot the exact solution
plt.plot(x, uexacte, 'k')

# Show the plot
plt.show()
