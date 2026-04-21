# Import
import random
import numpy as np
import matplotlib.pyplot as plt

# PARAMÈTRES
N_calcul = 30000       # Nombre de point pour le calcul
N_points_visibles = 1000  # Nombre de point visible sur le schéma 3D

a, b = 0, 1
c, d = 0, 1
h = 2

def f(x, y):
    return 1 + 0.5 * np.sin(np.pi * x) * np.cos(np.pi * y)

# Calcule méthode MONTE CARLO
inside = 0

points_in = []
points_out = []

for _ in range(N_calcul):
    x = random.uniform(a, b)
    y = random.uniform(c, d)
    z = random.uniform(0, h)

    if z <= f(x, y):
        inside += 1
        if len(points_in) < N_points_visibles // 2:
            points_in.append((x, y, z))
    else:
        if len(points_out) < N_points_visibles // 2:
            points_out.append((x, y, z))

volume_boite = (b - a) * (d - c) * h
volume_estime = volume_boite * inside / N_calcul

print("##### RÉSULTAT #####")
print(f"Points générés : {N_calcul}")
print(f"Points sous la surface : {inside}")
print(f"Volume estimé : {volume_estime:.6f}")

# Surface 3D
resolution = 18
X = np.linspace(a, b, resolution)
Y = np.linspace(c, d, resolution)
X, Y = np.meshgrid(X, Y)
Z = f(X, Y)

# Affichage
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Surface en filaire = beaucoup plus fluide
ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1)

# Afficher peu de points
if points_in:
    x_in, y_in, z_in = zip(*points_in)
    ax.scatter(x_in, y_in, z_in, s=6, depthshade=False, label="Sous surface")

if points_out:
    x_out, y_out, z_out = zip(*points_out)
    ax.scatter(x_out, y_out, z_out, s=6, depthshade=False, label="Au-dessus")

# Limites
ax.set_xlim(a, b)
ax.set_ylim(c, d)
ax.set_zlim(0, h)

# Labels
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title(f"Monte Carlo 3D - Volume ≈ {volume_estime:.4f}")

# Vue initiale
ax.view_init(elev=25, azim=40)

# Allègement pour meilleure fluidité
ax.grid(False)

plt.tight_layout()
plt.legend()
plt.show()