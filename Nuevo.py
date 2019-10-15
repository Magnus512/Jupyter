import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bokeh.io import output_notebook
from bokeh.io import show
from bokeh.plotting import figure
output_notebook() #Inline bokeh plots
#Cargar datos del documento
excelfile=pd.read_csv('Files/660nm.csv')
#Delimitar datos a utilizar por longitud de onda
excelfile=excelfile[(excelfile['Longitud'] > 500) & (excelfile['Longitud'] < 800)]
#Creando arreglos
wave = excelfile['Longitud']
wave = np.array(wave)
X = excelfile['Amplitud']
X = np.array(X)
Xmax = np.amax(X)
Xmin = np.amin(X)
Amplitud = (X-Xmin)/(Xmax-Xmin)
wavelist = np.array(wave.tolist())
Amplitudlist = np.array(Amplitud.tolist())
dfwave = pd.DataFrame(wavelist)
dfamplitud = pd.DataFrame(Amplitudlist)
data = {'Longitud':[dfwave],'Amplitud':[dfamplitud]}
df = pd.DataFrame(data)
#point = df.loc[df.Amplitud > 0.9]
#print(point)
#plt.figure(figsize=(10,10))
#plt.plot(wave,Amplitud)
#plt.minorticks_on()
#plt.grid(which='major',linestyle='-')
#plt.grid(which='minor',linestyle=':')
#plt.xlim(560,760)
#plt.ylim(0,1)
#plt.xlabel('Longitud de onda', fontsize=18)
#plt.ylabel('Amplitud', fontsize=18)
#plt.title('Espectro normalizado 660nm', fontsize=18)
p = figure (height=600,width=600,x_range=(560,760), y_range=(0,1.1),)
p.ygrid.minor_grid_line_color = 'blue'
p.ygrid.minor_grid_line_alpha = 0.05
p.xgrid.minor_grid_line_color = 'blue'
p.xgrid.minor_grid_line_alpha = 0.05
p.line(x=wave, y=Amplitud)
show(p)
#plt.savefig('Graphs/660norm.jpg')