"""
Azonos típusú rugók soros-és párhuzamos kapcsolása
"""

import numpy as np
import matplotlib.pyplot as plt

# Adatok definiálása: tömeg, nyúlás, erő
data1 = [
    [90.0, 160.0, 1.6],
    [64.0, 100.0, 1.0]
]

# Az adatok átalakítása NumPy tömbbé
data_array1 = np.array(data1)

# Külön array-ek kinyerése
nyulas1 = data_array1[:, 0]
tomeg1 = data_array1[:, 1]
ero1 = data_array1[:, 2]

# Második adatok definiálása: tömeg, nyúlás, erő
data2 = [
    [337.0, 160.0, 1.6],
    [209.0, 100.0, 1.0]
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

# Az azonos típusú rugók soros- és párhuzamos kapcsolásának ábrázolása
plt.plot(tomeg1, nyulas1, 'o--', color='red', label=r'Párhuzamos kapcsolás')
plt.plot(tomeg2, nyulas2, 'o--', color='blue', label=r'Soros kapcsolás')

# X és Y tengely feliratok beállítása
plt.xlabel(r'$m$ (g)', fontsize=font + 3)
plt.ylabel(r'$\Delta l$ (mm)', fontsize=font + 3)

# Ábrázolás címe
plt.title(r'Azonos típusú rugók soros- és párhuzamos kapcsolása', fontsize=font + 3)

# Rács bekapcsolása
plt.grid()

# Jelmagyarázat hozzáadása
plt.legend(fontsize=font)

# X és Y tengely feliratok méretének beállítása
plt.xticks(fontsize=font - 1)
plt.yticks(fontsize=font - 1)

# Ábra mentése PDF formátumban
plt.savefig('Kapcsolas', format='pdf')

# Ábra megjelenítése
plt.show()
