import sys 
sys.path.insert(1,'dsp-modulo')

from tkinter import *
from tkinter.filedialog import askopenfilename

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from thinkdsp import read_wave
import numpy

ventana = Tk()
ventana.title("La ventana")
ventana.geometry("800x600")

afinacion = StringVar()

def afinar():
    afinacion.set("Aprieta la cuerda")

btnCalcular = Button(ventana, text = "Inicio", command = afinar)
btnCalcular.pack()

primeraCuerda = Label(ventana, textvariable = afinacion)
primeraCuerda.pack()

ventana.mainloop()