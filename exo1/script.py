import numpy as np
import os



os.chdir(r"C:\Ecole\Python\eval\exo1")



# Exercice 1
tmin = np.genfromtxt('tmin.csv', delimiter=',').tolist()
tmax = np.genfromtxt('tmax.csv', delimiter=',').tolist()
tmoy = np.genfromtxt('tmoy.csv', delimiter=',').tolist()

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

tdelta 