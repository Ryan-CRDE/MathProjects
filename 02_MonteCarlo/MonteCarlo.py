# import
import random
import matplotlib.pyplot as plt

# Nombre de points aléatoires
n = 5000

# Listes pour stocker les points
x_dans = []
y_dans = []
x_hors = []
y_hors = []

# Compteur de points dans le quart de cercle
dans_cercle = 0

for _ in range(n):
    x = random.random()   # nombre aléatoire entre 0 et 1
    y = random.random()

    # Vérifie si le point est dans le quart de cercle
    if x**2 + y**2 <= 1:
        dans_cercle += 1
        x_dans.append(x)
        y_dans.append(y)
    else:
        x_hors.append(x)
        y_hors.append(y)

# Approximation de pi
pi_estime = 4 * dans_cercle / n

print(f"Estimation de pi = {pi_estime}")

# Tracé graphique
plt.figure(figsize=(6, 6))
plt.scatter(x_dans, y_dans, s=5, label="Dans le quart de cercle")
plt.scatter(x_hors, y_hors, s=5, label="Hors du quart de cercle")

plt.title(f"Méthode de Monte Carlo : estimation de pi ≈ {pi_estime}")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.legend()
plt.show()