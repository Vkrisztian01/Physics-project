"""
A periódusidő a tömeg gyöke ellenében
"""

import matplotlib.pyplot as plt
import numpy as np

# Given data
data2 = [
    [0.000, -1.155e-2],
    [0.040, -1.077e-2],
    [0.080, -6.511e-3],
    [0.120, 7.710e-5],
    [0.160, 8.215e-3],
    [0.200, 1.790e-2],
    [0.240, 2.914e-2],
    [0.280, 3.805e-2],
    [0.320, 4.580e-2],
    [0.360, 5.239e-2],
    [0.400, 5.549e-2],
    [0.440, 5.549e-2],
    [0.480, 5.123e-2],
    [0.520, 4.580e-2],
    [0.560, 3.650e-2],
    [0.600, 2.682e-2],
    [0.640, 1.519e-2],
    [0.680, 5.890e-3],
    [0.720, -3.023e-3],
    [0.760, -8.448e-3],
    [0.800, -1.155e-2],
    [0.840, -9.998e-3],
    [0.880, -5.736e-3],
    [0.920, 1.240e-3],
    [0.960, 8.990e-3],
    [1.000, 2.023e-2],
    [1.040, 2.953e-2],
    [1.080, 3.883e-2],
    [1.120, 4.774e-2],
    [1.160, 5.317e-2],
    [1.200, 5.510e-2],
    [1.240, 5.472e-2],
    [1.280, 5.084e-2],
    [1.320, 4.464e-2],
    [1.360, 3.573e-2],
    [1.400, 2.527e-2],
    [1.440, 1.403e-2],
    [1.480, 4.340e-3],
    [1.520, -3.798e-3],
    [1.560, -9.223e-3],
    [1.600, -1.116e-2],
    [1.640, -9.611e-3],
    [1.680, -5.348e-3],
    [1.720, 2.402e-3],
    [1.760, 1.054e-2],
    [1.800, 2.100e-2],
    [1.840, 3.108e-2],
    [1.880, 4.038e-2],
    [1.920, 4.813e-2],
    [1.960, 5.278e-2],
    [2.000, 5.549e-2],
    [2.040, 5.394e-2],
    [2.080, 5.007e-2],
    [2.120, 4.270e-2],
    [2.160, 3.379e-2],
    [2.200, 2.372e-2],
    [2.240, 1.287e-2],
    [2.280, 3.177e-3],
    [2.320, -5.348e-3],
    [2.360, -1.039e-2],
    [2.400, -1.155e-2],
    [2.440, -9.611e-3],
    [2.480, -4.573e-3],
    [2.520, 2.790e-3],
    [2.560, 1.209e-2],
    [2.600, 2.255e-2],
    [2.640, 3.224e-2],
    [2.680, 4.154e-2],
    [2.720, 4.890e-2],
    [2.760, 5.355e-2],
    [2.800, 5.510e-2],
    [2.840, 5.317e-2],
    [2.880, 4.890e-2],
    [2.920, 4.232e-2],
    [2.960, 3.302e-2],
    [3.000, 2.294e-2],
    [3.040, 1.015e-2],
    [3.080, 1.240e-3],
    [3.120, -6.511e-3],
    [3.160, -1.077e-2],
    [3.200, -1.155e-2]
]

# Convert the data to a NumPy array
data_array2 = np.array(data2)

# Extract individual arrays
t= data_array2[:, 0]
y = data_array2[:, 1]


# Ábrázolás előkészítése
font = 12
plt.figure(figsize=(8, 5))

# A periódusidő a tömeg gyöke ellenében ábrázolása
#plt.plot(t, y, '.', color='green') --eredeti
plt.plot(t, y, color='green')

# X és Y tengely feliratok beállítása
plt.xlabel(r't (s)', fontsize=font + 3)
plt.ylabel(r'y (m)', fontsize=font + 3)

# Ábrázolás címe
plt.title(r'A kitérések hullámfüggvénye', fontsize=font + 3)

# Rács bekapcsolása
plt.grid()

# Jelmagyarázat hozzáadása
plt.legend(fontsize=font)

# X és Y tengely feliratok méretének beállítása
plt.xticks(fontsize=font - 1)
plt.yticks(fontsize=font - 1)

# Ábra mentése PDF formátumban
plt.savefig('kiteresazidoben', format='pdf')

# Ábra megjelenítése
plt.show()
