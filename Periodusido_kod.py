"""
A periódusidő a tömeg gyöke ellenében
"""

import numpy as np
import matplotlib.pyplot as plt

# Adatok definiálása: tömeg, tömeg gyök, mért idő, periódus idő
data1 = [
    [40.0, 6.3246, 9.09, 0.4545],
    [60.0, 7.7459, 10.97, 0.5485],
    [80.0, 8.9443, 12.41, 0.6205],
    [100.0, 10.0, 13.69, 0.6840],
    [120.0, 10.9545, 14.94, 0.747],
    [140.0, 11.8323, 15.94, 0.797],
    [160.0, 12.6491, 19.54, 0.827]
]

# Az adatok átalakítása NumPy tömbbé
data_array1 = np.array(data1)

# Külön array-ek kinyerése
tomeg = data_array1[:, 0]
tomeggyok = data_array1[:, 1]
mertido = data_array1[:, 2]
periodusido = data_array1[:, 3]

# Ábrázolás előkészítése
font = 12
plt.figure(figsize=(8, 5))

# A periódusidő a tömeg gyöke ellenében ábrázolása
plt.plot(tomeggyok, periodusido, 'o--', color='red', label=r'Rezgések')

# X és Y tengely feliratok beállítása
plt.xlabel(r'$\sqrt{m}$ ($\sqrt{g}$)', fontsize=font + 3)
plt.ylabel(r'T (s)', fontsize=font + 3)

# Ábrázolás címe
plt.title(r'A periódusok ideje a tömeg gyöke ellenében', fontsize=font + 3)

# Rács bekapcsolása
plt.grid()

# Jelmagyarázat hozzáadása
plt.legend(fontsize=font)

# X és Y tengely feliratok méretének beállítása
plt.xticks(fontsize=font - 1)
plt.yticks(fontsize=font - 1)

# Ábra mentése PDF formátumban
plt.savefig('Periodus', format='pdf')

# Ábra megjelenítése
plt.show()
