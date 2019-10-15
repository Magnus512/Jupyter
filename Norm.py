#Importar librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#Definicion de funciones
def peak(x, c):
    return np.exp(-np.power( x -c, 2) / 16.0)

def lin_interp(x, y, i, half):
    return x[i] + (x[i+1] - x[i]) * ((half - y[i]) / (y[i+1] - y[i]))

def half_max_x(x, y):
    half = max(y)/2.0
    signs = np.sign(np.add(y, -half))
    zero_crossings = (signs[0:-2] != signs[1:-1])
    zero_crossings_i = np.where(zero_crossings)[0]
    return [lin_interp(x, y, zero_crossings_i[0], half), lin_interp(x, y, zero_crossings_i[1], half)]

#Cargar datos del documento
excelfile=pd.read_csv('Files/6602nm.csv')
#Delimitar datos a utilizar por longitud de onda
excelfile=excelfile[(excelfile['Longitud'] > 500) & (excelfile['Longitud'] < 800)]
#Creando arreglos
wave = excelfile['Longitud']
wave = wave.to_numpy()
Y = excelfile['Amplitud']

#Suevizado de datos
Y = signal.savgol_filter(Y,53,3)
Ymax = np.amax(Y)
Ymin = np.amin(Y)
Amplitud = (Y-Ymin)/(Ymax-Ymin)

#FWHM
hmx = half_max_x(wave, Amplitud)
fwhm = hmx[1] - hmx[0]
print("FWHM: {:.3f}nm".format(fwhm))
half = max(Amplitud)/2.0

#PLOT
plt.figure(figsize=(10,10))
plt.plot(wave,Amplitud)
plt.plot(hmx, [half, half], label = "FWHM")
plt.legend()
plt.minorticks_on()
plt.grid(which='major',linestyle='-')
plt.grid(which='minor',linestyle=':')
plt.xlim(560,760)
plt.ylim(0,1)
plt.xlabel('Longitud de onda', fontsize=18)
plt.ylabel('Amplitud', fontsize=18)
plt.title('Espectro normalizado 660nm', fontsize=18)
plt.savefig('Graphs/6603norm.png')

#Cargar datos
excelfile=pd.read_csv('Files/7802nm.csv')
excelfile=excelfile[(excelfile['Longitud'] > 600) & (excelfile['Longitud'] < 900)]
#Crear Arreglos
wave = excelfile['Longitud']
wave = wave.to_numpy()
Y = excelfile['Amplitud']

#Suevizado de datos
Y = signal.savgol_filter(Y,53,3)
Ymax = np.amax(Y)
Ymin = np.amin(Y)
Amplitud = (Y-Ymin)/(Ymax-Ymin)

#FWHM
hmx = half_max_x(wave, Amplitud)
fwhm = hmx[1] - hmx[0]
print("FWHM: {:.3f}nm".format(fwhm))
half = max(Amplitud)/2.0

plt.figure(figsize=(10,10))
plt.plot(wave,Amplitud)
plt.plot(hmx, [half, half], label = "FWHM")
plt.legend()
plt.minorticks_on()
plt.grid(which='major',linestyle='-')
plt.grid(which='minor',linestyle=':')
plt.xlim(680,880)
plt.ylim(0,1.1)
plt.xlabel('Longitud de onda', fontsize=18)
plt.ylabel('Amplitud', fontsize=18)
plt.title('Espectro normalizado 780nm', fontsize=18)
plt.savefig('Graphs/780norm.png')

excelfile=pd.read_csv('Files/8082nm.csv');
excelfile=excelfile[(excelfile['Longitud'] > 700) & (excelfile['Longitud'] < 950)]
#Crear Arreglos
wave = excelfile['Longitud']
wave = wave.to_numpy()
Y = excelfile['Amplitud']

#Suevizado de datos
Y = signal.savgol_filter(Y,53,3)
Ymax = np.amax(Y)
Ymin = np.amin(Y)
Amplitud = (Y-Ymin)/(Ymax-Ymin)

#FWHM
hmx = half_max_x(wave, Amplitud)
fwhm = hmx[1] - hmx[0]
print("FWHM: {:.3f}nm".format(fwhm))
half = max(Amplitud)/2.0

#Plot
plt.figure(figsize=(10,10))
plt.plot(wave,Amplitud)
plt.plot(hmx, [half, half], label = "FWHM")
plt.legend()
plt.minorticks_on()
plt.grid(which='major',linestyle='-')
plt.grid(which='minor',linestyle=':')
plt.xlabel('Longitud de onda', fontsize=18)
plt.xlim(708,908)
plt.ylim(0,1.1)
plt.ylabel('Amplitud', fontsize=18)
plt.title('Espectro normalizado 808nm', fontsize=18)
plt.savefig('Graphs/8082norm.png')

excelfile=pd.read_csv('Files/8502nm.csv')
excelfile=excelfile[(excelfile['Longitud'] > 700) & (excelfile['Longitud'] < 950)]
#Crear Arreglos
wave = excelfile['Longitud']
wave = wave.to_numpy()
Y = excelfile['Amplitud']

#Suevizado de datos
Y = signal.savgol_filter(Y,53,3)
Ymax = np.amax(Y)
Ymin = np.amin(Y)
Amplitud = (Y-Ymin)/(Ymax-Ymin)

#FWHM
hmx = half_max_x(wave, Amplitud)
fwhm = hmx[1] - hmx[0]
print("FWHM: {:.3f}nm".format(fwhm))
half = max(Amplitud)/2.0

#Plot
plt.figure(figsize=(10,10))
plt.plot(wave,Amplitud)
plt.plot(hmx, [half, half], label = "FWHM")
plt.legend()
plt.minorticks_on()
plt.grid(which='major',linestyle='-')
plt.grid(which='minor',linestyle=':')
plt.xlabel('Longitud de onda', fontsize=18)
plt.xlim(740,940)
plt.ylim(0,1.1)
plt.ylabel('Amplitud', fontsize=18)
plt.title('Espectro normalizado 850nm', fontsize=18)
plt.savefig('Graphs/850norm.png')
