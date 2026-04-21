# Import
import statistics
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Données d'entrée
data = [5, 5, 4, 3, 5, 4.5, 3.5, 5, 5, 5.5, 2]

# Calculs de la moyenne, de la mediane et de la variance
moyenne = statistics.mean(data)
mediane = statistics.median(data)
variance = statistics.pvariance(data)

# Affichage des résultats dans le CMD
# print(f"Moyenne : {moyenne:.2f}")
# print(f"Médiane : {mediane:.2f}")
# print(f"Variance : {variance:.2f}")

# Création de la courbe (graphique)
kde = gaussian_kde(data)
x = np.linspace(min(data)-5, max(data)+5, 200)
y = kde(x)

# Création du graphique
plt.figure(figsize=(8,5))

# Configuration de la courbe (graphique)
plt.plot(x, y, linewidth=3, label="Distribution")

# Lignes affichant la moyenne, la médiane et la variance (graphique)
plt.axvline(moyenne, linestyle="-", linewidth=2, label=f"Moyenne = {moyenne:.2f}")
plt.axvline(mediane, linestyle="--", linewidth=1, label=f"Médiane = {mediane:.2f}")
plt.axvline(variance, linestyle="--", linewidth=2, label=f"Variance = {variance:.2f}")

# Affichage des titres (graphique)
plt.title("Courbe graphique)")
plt.xlabel("Valeurs")
plt.ylabel("Fréquence")

# Ajout des légendes (graphique)
plt.legend()

# Affichage de la grille (graphique)
plt.grid(True, linestyle="--", alpha=0.5)

# Affichage du graphique
plt.show()
