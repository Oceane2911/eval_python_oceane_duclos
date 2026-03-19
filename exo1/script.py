import numpy as np
import os
import matplotlib.pyplot as plt




os.chdir(r"C:\Ecole\Python\eval\exo1")



# Exercice 1
tmin = np.genfromtxt('data/2016/tmin.csv', delimiter=',').tolist()
tmax = np.genfromtxt('data/2016/tmax.csv', delimiter=',').tolist()
tmoy = np.genfromtxt('data/2016/tmoy.csv', delimiter=',').tolist()

# print("Tmin :", tmin)
# print("Tmax :", tmax)
# print("Tmoy :", tmoy)

# Exercice 2


tmin_array = np.array(tmin)
tmax_array = np.array(tmax)
tmoy_array = np.array(tmoy)

tab = np.column_stack((tmin_array, tmax_array, tmoy_array))

# print(tab)

# Execerci 3


tdelta = tab[:, 1] - tab[:, 0]

tab = np.column_stack((tab, tdelta))

# print(tab)

# Exercice 4
tableaux ={}
tableaux[2016] = tab
for annee in range(2017, 2023):
    tmin = np.genfromtxt(f'data/{annee}/tmin.csv', delimiter=',').tolist()
    tmax = np.genfromtxt(f'data/{annee}/tmax.csv', delimiter=',').tolist()
    tmoy = np.genfromtxt(f'data/{annee}/tmoy.csv', delimiter=',').tolist()

    tmin_array = np.array(tmin)
    tmax_array = np.array(tmax)
    tmoy_array = np.array(tmoy)

    tab_annee = np.column_stack((tmin_array, tmax_array, tmoy_array))
    tdelta = tab_annee[:, 1] - tab_annee[:, 0]
    tab_annee = np.column_stack((tab_annee, tdelta))

    tableaux[annee] = tab_annee  

# Exercice 5 - Statistiques par année

for annee, tab_annee in tableaux.items():
    tmax_annee        = np.max(tab_annee[:, 1])
    jour_plus_chaud   = np.argmax(tab_annee[:, 1])
    tmin_jour_chaud   = tab_annee[jour_plus_chaud, 0]
    tmoy_annee        = np.mean(tab_annee[:, 2])
    tmoy_delta        = np.mean(tab_annee[:, 3])


print(tmax_annee,tmin_jour_chaud, tmoy_annee, tmoy_delta)


# Exercice 6


# Exercice 7

