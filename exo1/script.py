import numpy as np
import os



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

for i in range(6):
    val = 2017 +i
    tmin = np.genfromtxt('data/'+str(val)+'/tmin.csv', delimiter=',').tolist()
    tmax = np.genfromtxt('data/'+str(val)+'/tmax.csv', delimiter=',').tolist()
    tmoy = np.genfromtxt('data/'+str(val)+'/tmoy.csv', delimiter=',').tolist()
    # print("Tmin :", tmin)
    # print("Tmax :", tmax)
    # print("Tmoy :", tmoy)

    tmin_array = np.array(tmin)
    tmax_array = np.array(tmax)
    tmoy_array = np.array(tmoy)

    tab = np.column_stack((tmin_array, tmax_array, tmoy_array))
    tdelta = tab[:, 1] - tab[:, 0]

    tab = np.column_stack((tab, tdelta))
    print(tab)

# Exercice 5