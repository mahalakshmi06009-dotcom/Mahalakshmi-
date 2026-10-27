import matplotlib.pyplot as plt

# Un reading - itha maathi un original reading potuko
volume = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
emf = [302, 307, 318, 330, 344, 368, 380, 384, 394, 410, 430, 715, 735, 743, 752, 753, 756, 770, 775]

plt.figure(figsize=(8,10))
plt.plot(volume, emf, 'o-', color='black', linewidth=1, markersize=6)
plt.axvline(x=11, color='black', linestyle='--', linewidth=1) # End point dotted line

plt.xlabel('Volume of K2Cr2O7 (ml)')
plt.ylabel('EMF (mV)')
plt.title('Potentiometric Titration - Fe2+ vs K2Cr2O7')
plt.grid(True, linestyle='--', alpha=0.6)
plt.xlim(0, 22)
plt.ylim(0, 800)

# Arrow mark
plt.annotate('End Point\n11 ml', xy=(11, 0), xytext=(13, 150),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.savefig('graph.png', dpi=300)
plt.show()

# Calculation
V1 = 11
N1 = (V1 * 0.1) / 20
print(f"Normal
