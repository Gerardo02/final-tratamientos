from tkinter import *
#import analisis_tiempo_real as atr
import pyaudio 
import numpy as np  
import wave 


ventana = Tk()
ventana.title("La ventana")
ventana.geometry("800x600")

#Formato de audio de microfono
PROFUNDIDAD_BITS = pyaudio.paInt16
CANALES = 1
FRECUENCIA_MUESTREO = 44100
TIEMPO_GRABACION = 1

#Tamano de Chunk
CHUNK = 2048




afinacion = StringVar()

def iniciar():
    afinacion.set("Aprieta la cuerda")
    if __name__ == "__main__":
        p = pyaudio.PyAudio()
        stream = p.open(format = PROFUNDIDAD_BITS, channels = CANALES, rate = FRECUENCIA_MUESTREO, input = True, frames_per_buffer = CHUNK)

        for i in range(0, int(FRECUENCIA_MUESTREO * TIEMPO_GRABACION / CHUNK ))







btnCalcular = Button(ventana, text = "Inicio", command = iniciar)
btnCalcular.pack()

primeraCuerda = Label(ventana, textvariable = afinacion)
primeraCuerda.pack()

ventana.mainloop()
