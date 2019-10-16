#Importar librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import scipy

dataframe=pd.read_csv('Files/660nuevo.csv')

#print(dataframe)

tiempo = dataframe['Tiempo']
corriente = dataframe['Corriente']
voltaje = dataframe['Voltaje']

corriente = corriente*1000

#Separamos todos los voltajes
voltaje1 = voltaje[1:30:1]
voltaje2 = voltaje[32:60:1]
voltaje3 = voltaje[62:90:1]
voltaje4 = voltaje[92:120:1]
voltaje5 = voltaje[122:150:1]
voltaje6 = voltaje[152:180:1]
voltaje7 = voltaje[182:210:1]
voltaje8 = voltaje[212:240:1]
voltaje9 = voltaje[242:270:1]
voltaje10 = voltaje[272:300:1]
voltaje11 = voltaje[302:330:1]
voltaje12 = voltaje[332:360:1]

#Separamos todas las corrientes
corriente1 = corriente[1:30:1]
corriente2 = corriente[32:60:1]
corriente3 = corriente[62:90:1]
corriente4 = corriente[92:120:1]
corriente5 = corriente[122:150:1]
corriente6 = corriente[152:180:1]
corriente7 = corriente[182:210:1]
corriente8 = corriente[212:240:1]
corriente9 = corriente[242:270:1]
corriente10 = corriente[272:300:1]
corriente11 = corriente[302:330:1]
corriente12 = corriente[332:360:1]

#valores medios y deviaciones estandar
#voltaje
voltajemed1 = np.mean(voltaje1)
voltajemed2 = np.mean(voltaje2)
voltajemed3 = np.mean(voltaje3)
voltajemed4 = np.mean(voltaje4)
voltajemed5 = np.mean(voltaje5)
voltajemed6 = np.mean(voltaje6)
voltajemed7 = np.mean(voltaje7)
voltajemed8 = np.mean(voltaje8)
voltajemed9 = np.mean(voltaje9)
voltajemed10 = np.mean(voltaje10)
voltajemed11 = np.mean(voltaje11)
voltajemed12 = np.mean(voltaje12)

#Corrientes
corrientemed1 = np.mean(corriente1)
corrientemed2 = np.mean(corriente2)
corrientemed3 = np.mean(corriente3)
corrientemed4 = np.mean(corriente4)
corrientemed5 = np.mean(corriente5)
corrientemed6 = np.mean(corriente6)
corrientemed7 = np.mean(corriente7)
corrientemed8 = np.mean(corriente8)
corrientemed9 = np.mean(corriente9)
corrientemed10 = np.mean(corriente10)
corrientemed11 = np.mean(corriente11)
corrientemed12 = np.mean(corriente12)

#Desvi Corrientes
desvcorr1 = np.std(corriente1)
desvcorr2 = np.std(corriente2)
desvcorr3 = np.std(corriente3)
desvcorr4 = np.std(corriente4)
desvcorr5 = np.std(corriente5)
desvcorr6 = np.std(corriente6)
desvcorr7 = np.std(corriente7)
desvcorr8 = np.std(corriente8)
desvcorr9 = np.std(corriente9)
desvcorr10 = np.std(corriente10)
desvcorr11 = np.std(corriente11)
desvcorr12 = np.std(corriente12)

#arreglos
voltajes = np.array([voltajemed1, voltajemed2, voltajemed3, voltajemed4, voltajemed5, voltajemed6, voltajemed7, voltajemed8, voltajemed9, voltajemed10, voltajemed11, voltajemed12])
corrientes = np.array([corrientemed1, corrientemed2, corrientemed3, corrientemed4, corrientemed5, corrientemed6, corrientemed7, corrientemed8, corrientemed9, corrientemed10, corrientemed11, corrientemed12])
desvcorrientes = np.array([desvcorr1, desvcorr2, desvcorr3, desvcorr4, desvcorr5, desvcorr6, desvcorr7, desvcorr8, desvcorr9, desvcorr10, desvcorr11, desvcorr12,])
print(voltajes)
print(corrientes)
print(desvcorrientes)
plt.figure(figsize=(50,50))
plt.errorbar(voltajes, corrientes, yerr=desvcorrientes)
plt.show()