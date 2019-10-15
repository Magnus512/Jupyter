import tkinter as tk
import serial

#serial.Serial('COM3','baudrate',115200)

def Iniciar():
    print("Hola mundo")

def TomarClicked():
    print("Adios")

win = tk.Tk()

win.title("Oximetro")
frame = tk.Frame(win)
frame.pack()

tk.Button(frame, text="Tomar", command=Iniciar).pack()

win.mainloop()