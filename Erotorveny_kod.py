"""
A rugómegnyúlások tömeg ellenében
"""

# Szükséges modulok importálása
import numpy as np
import matplotlib.pyplot as plt

# Első adatok definiálása: nyúlás, tömeg, erő
data1 = [
    [23.0, 20.0, 0.2],
    [45.0, 40.0, 0.4],
    [66.0, 60.0, 0.6],
    [85.0, 80.0, 0.8],
    [106.0, 100.0, 1.0],
    [125.0, 120.0, 1.2]
]

# Az adatok átalakítása NumPy tömbbé
data_array1 = np.array(data1)

# Külön array-ek kinyerése
nyulas1 = data_array1[:, 0]
tomeg1 = data_array1[:, 1]
ero1 = data_array1[:, 2]

# Második adatok definiálása: nyúlás, tömeg, erő
data2 = [
    [18.0, 40.0, 0.4],
    [34.0, 80.0, 0.8],
    [46.0, 120.0, 1.2],
    [64.0, 160.0, 1.6],
    [78.0, 200.0, 2.0],
    [96.0, 240.0, 2.4],
    [112.0, 280.0, 2.8]
]

# Az adatok átalakítása NumPy tömbbé
data_array2 = np.array(data2)

# Külön array-ek kinyerése
nyulas2 = data_array2[:, 0]
tomeg2 = data_array2[:, 1]
ero2 = data_array2[:, 2]

# Ábrázolás előkészítése
font = 12
plt.figure()

# Az első rugó adatainak ábrázolása
plt.plot(tomeg1, nyulas1, 'o--', color='red', label=r'I. rugó')

# A második rugó adatainak ábrázolása
plt.plot(tomeg2, nyulas2, 'o--', color='blue', label=r'II. rugó')

# X és Y tengely feliratok beállítása
plt.xlabel(r'$m$ (g)', fontsize=font + 3)
plt.ylabel(r'$\Delta l$ (mm)', fontsize=font + 3)

# Ábrázolás címe
plt.title(r'A rugómegnyúlások tömeg ellenében', fontsize=font + 3)

# Rács bekapcsolása
plt.grid()

# Jelmagyarázat hozzáadása
plt.legend(fontsize=font)

# X és Y tengely feliratok méretének beállítása
plt.xticks(fontsize=font - 1)
plt.yticks(fontsize=font - 1)

# Ábra mentése PDF formátumban
plt.savefig('Direkciosallando', format='pdf')

# Ábra megjelenítése
plt.show()
