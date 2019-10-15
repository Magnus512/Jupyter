# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% [markdown]
# # Normalización de longitudes de onda
#%% [markdown]
# Se utiliza pandas y numpy para crear el Dataframe y los arreglos necesarios, pandas permite seleccionar solo los datos dentro del rango de longitudes de ondas deseadas.  Utilizando la siguiente ecuacion es posible normalizar los datos de potencia entre [0-1]
# 
# \begin{equation*}
# X' = \frac{X-X_{min}}{X_{max}-X_{min}}
# \end{equation*}
# 

#%%
#Importar librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import signal

#%%
#Cargar datos del documento
excelfile=pd.read_csv('Files/6602nm.csv')
#Delimitar datos a utilizar por longitud de onda
excelfile=excelfile[(excelfile['Longitud'] > 500) & (excelfile['Longitud'] < 800)]
#Creando arreglos
wave = excelfile['Longitud']
X = excelfile['Amplitud']
#Suevizado de datos
X = signal.savgol_filter(X,53,5)
Xmax = np.amax(X)
Xmin = np.amin(X)
Amplitud = (X-Xmin)/(Xmax-Xmin)
plt.figure(figsize=(10,10))
plt.plot(wave,Amplitud)
plt.minorticks_on()
plt.grid(which='major',linestyle='-')
plt.grid(which='minor',linestyle=':')
plt.xlim(560,760)
plt.ylim(0,1)
plt.xlabel('Longitud de onda', fontsize=18)
plt.ylabel('Amplitud', fontsize=18)
plt.title('Espectro normalizado 660nm', fontsize=18)
plt.savefig('Graphs/6603norm.png')


#%%
excelfile=pd.read_csv('Files/7802nm.csv')
excelfile=excelfile[(excelfile['Longitud'] > 600) & (excelfile['Longitud'] < 900)]
wave = excelfile['Longitud']
X = excelfile['Amplitud']
#Suevizado de datos
X = signal.savgol_filter(X,53,5)
Xmax = np.amax(X)
Xmin = np.amin(X)
Amplitud = (X-Xmin)/(Xmax-Xmin)
plt.figure(figsize=(10,10))
plt.plot(wave,Amplitud)
plt.minorticks_on()
plt.grid(which='major',linestyle='-')
plt.grid(which='minor',linestyle=':')
plt.xlim(680,880)
plt.ylim(0,1.1)
plt.xlabel('Longitud de onda', fontsize=18)
plt.ylabel('Amplitud', fontsize=18)
plt.title('Espectro normalizado 780nm', fontsize=18)
plt.savefig('Graphs/780norm.png')


#%%
excelfile=pd.read_csv('Files/8082nm.csv');
excelfile=excelfile[(excelfile['Longitud'] > 700) & (excelfile['Longitud'] < 950)]
wave = excelfile['Longitud']
X = excelfile['Amplitud']
#Suevizado de datos
X = signal.savgol_filter(X,53,5)
Xmax = np.amax(X)
Xmin = np.amin(X)
Amplitud = (X-Xmin)/(Xmax-Xmin)
plt.figure(figsize=(10,10))
plt.plot(wave,Amplitud)
plt.minorticks_on()
plt.grid(which='major',linestyle='-')
plt.grid(which='minor',linestyle=':')
plt.xlabel('Longitud de onda', fontsize=18)
plt.xlim(708,908)
plt.ylim(0,1.1)
plt.ylabel('Amplitud', fontsize=18)
plt.title('Espectro normalizado 808nm', fontsize=18)
plt.savefig('Graphs/8082norm.png')


#%%
excelfile=pd.read_csv('Files/8502nm.csv')
excelfile=excelfile[(excelfile['Longitud'] > 700) & (excelfile['Longitud'] < 950)]
wave = excelfile['Longitud']
X = excelfile['Amplitud']
#Suevizado de datos
X = signal.savgol_filter(X,53,5)
Xmax = np.amax(X)
Xmin = np.amin(X)
Amplitud = (X-Xmin)/(Xmax-Xmin)
plt.figure(figsize=(10,10))
plt.plot(wave,Amplitud)
plt.minorticks_on()
plt.grid(which='major',linestyle='-')
plt.grid(which='minor',linestyle=':')
plt.xlabel('Longitud de onda', fontsize=18)
plt.xlim(740,940)
plt.ylim(0,1.1)
plt.ylabel('Amplitud', fontsize=18)
plt.title('Espectro normalizado 850nm', fontsize=18)
plt.savefig('Graphs/850norm.png')


#%%



