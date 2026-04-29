import random
import statistics
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Paramètres
C0 = 1000    # Capital initial (CHF)
x  = 100     # Mise par tour (CHF)
p  = 0.60    # Probabilité de gain (60 %)
N  = 10      # Nombre de jours par simulation
m  = 1000    # Nombre de simulations
SAMPLE = 30  # Nombre de trajectoires à afficher

# Simulation
echecs          = 0
capitaux_finaux = []
trajectoires    = []

for i in range(m):
    capital = C0
    chemin  = [capital]
    ruine   = False

    for jour in range(N):
        if capital <= 0:
            ruine = True
            break
        capital += x if random.random() < p else -x
        if capital < 0:
            capital = 0
        chemin.append(capital)

    if capital <= 0 or ruine:
        echecs += 1

    capitaux_finaux.append(capital)
    if i < SAMPLE:
        trajectoires.append(chemin)

# Stats
gain_moyen  = statistics.mean(capitaux_finaux)
gain_max    = max(capitaux_finaux)
prob_ruine  = echecs / m * 100
prob_profit = sum(1 for c in capitaux_finaux if c > C0) / m * 100

# Graphiques
fig = plt.figure(figsize=(12, 9))
fig.patch.set_facecolor('#f8f9fa')
gs  = gridspec.GridSpec(2, 1, figure=fig, hspace=0.45)

jours = list(range(N + 1))
colors = [
    '#378ADD','#1D9E75','#D85A30','#7F77DD','#D4537E',
    '#BA7517','#E24B4A','#0F6E56','#534AB7','#993C1D'
]

# Graphique 1 : Trajectoires
ax1 = fig.add_subplot(gs[0])
ax1.set_facecolor('#ffffff')

for i, chemin in enumerate(trajectoires):
    jours_path = list(range(len(chemin)))
    ax1.plot(jours_path, chemin,
             color=colors[i % len(colors)],
             linewidth=0.9, alpha=0.7)

ax1.axhline(y=C0, color='#888780', linewidth=1.5,
            linestyle='--', label=f'Capital initial ({C0} CHF)')
ax1.axhline(y=gain_moyen, color='#2c2c2a', linewidth=1.5,
            linestyle=':', label=f'Moyenne finale ({gain_moyen:.0f} CHF)')

ax1.set_xlim(0, N)
ax1.set_ylim(bottom=0)
ax1.set_xlabel('Jour', fontsize=12)
ax1.set_ylabel('Capital (CHF)', fontsize=12)
ax1.set_title(f'Trajectoires ({SAMPLE} simulations sur {m})', fontsize=13, fontweight='bold', pad=10)
ax1.legend(fontsize=10, framealpha=0.9)
ax1.grid(True, linestyle='--', linewidth=0.4, alpha=0.5)
ax1.spines[['top','right']].set_visible(False)

# Graphique 2 : Distribution des capitaux finaux
ax2 = fig.add_subplot(gs[1])
ax2.set_facecolor('#ffffff')

bins = 30
n_vals, bin_edges, patches = ax2.hist(capitaux_finaux, bins=bins, edgecolor='white', linewidth=0.5)

for patch, left_edge in zip(patches, bin_edges[:-1]):
    patch.set_facecolor('#E24B4A' if left_edge < C0 else '#1D9E75')

ax2.axvline(x=C0, color='#888780', linewidth=1.5,
            linestyle='--', label=f'Capital initial ({C0} CHF)')
ax2.axvline(x=gain_moyen, color='#2c2c2a', linewidth=1.5,
            linestyle=':', label=f'Moyenne ({gain_moyen:.0f} CHF)')

from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#1D9E75', label=f'Gain  ({prob_profit:.1f}%)'),
    Patch(facecolor='#E24B4A', label=f'Perte ({100-prob_profit:.1f}%)'),
    plt.Line2D([0],[0], color='#888780', linestyle='--', label=f'Capital initial ({C0} CHF)'),
    plt.Line2D([0],[0], color='#2c2c2a', linestyle=':',  label=f'Moyenne ({gain_moyen:.0f} CHF)'),
]
ax2.legend(handles=legend_elements, fontsize=10, framealpha=0.9)

ax2.set_xlabel('Capital final (CHF)', fontsize=12)
ax2.set_ylabel('Nombre de simulations', fontsize=12)
ax2.set_title('Distribution des capitaux finaux', fontsize=13, fontweight='bold', pad=10)
ax2.grid(True, axis='y', linestyle='--', linewidth=0.4, alpha=0.5)
ax2.spines[['top','right']].set_visible(False)

# Titre global + stats
fig.suptitle(
    f'Marche aléatoire — C₀={C0} CHF  |  x={x} CHF  |  p={p*100:.0f}%  |  '
    f'N={N} jours  |  m={m} simulations\n'
    f'Moyenne={gain_moyen:.0f} CHF  |  Max={gain_max:.0f} CHF  |  '
    f'Probabilité de ruine={prob_ruine:.1f}%',
    fontsize=11, y=0.98, color='#2c2c2a'
)

plt.savefig('simulation_graphique.png', dpi=150, bbox_inches='tight',
            facecolor=fig.get_facecolor())
print("Graphique sauvegardé : simulation_graphique.png")
plt.show()
