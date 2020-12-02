from tkinter import *
#import analisis_tiempo_real as atr
import pyaudio 
import numpy as np  
import wave 


ventana = Tk()
ventana.title("La ventana")
ventana.geometry("800x600")
ventana.configure(background='black')

#Formato de audio de microfono
PROFUNDIDAD_BITS = pyaudio.paInt16
CANALES = 1
FRECUENCIA_MUESTREO = 44100
TIEMPO_GRABACION = 1

#Tamano de Chunk
CHUNK = 2048



window = np.blackman(CHUNK)
stringCuerda = StringVar()
stringFrecuenciaA = StringVar()
stringFrecuencia = StringVar()
stringAfinacion = StringVar()


def iniciar():

    def analizar(stream):
        data = stream.read(CHUNK, exception_on_overflow = False)
        waveData = wave.struct.unpack("%dh"%(CHUNK), data)
        npData = np.array(waveData)

        dataEntrada = npData * window

        fftData = np.abs(np.fft.rfft(dataEntrada))
        indiceFrecuenciaDominante = fftData[1:].argmax() + 1

        y0,y1,y2 = np.log(fftData[indiceFrecuenciaDominante-1:indiceFrecuenciaDominante+2])
        x1 = (y2-y0) * 0.5 / (2 * y1 - y2 - y0)
        frecuenciaDominante = (indiceFrecuenciaDominante+x1) * FRECUENCIA_MUESTREO / CHUNK
        Frecuencia = str(frecuenciaDominante)
        print("Frecuencia Dominante: " + str(frecuenciaDominante) + " Hz", end='\r')
        stringFrecuencia.set(Frecuencia)

        tolerancia = 13.0
        toleranciaAfinada = 1.3
        
        if  frecuenciaDominante > 82.4 - tolerancia and frecuenciaDominante < 82.4 + tolerancia:
            Cuerda = "6ta Mi(E) 82.4 Hz"
            if  frecuenciaDominante > 82.4 - toleranciaAfinada and frecuenciaDominante < 82.4 + toleranciaAfinada:
                Afinacion = "La afinacion se oye bien"
            elif  frecuenciaDominante < 82.4 + toleranciaAfinada:
                Afinacion = "Se necesita apretar la cuerda"
            else:
                Afinacion = "Se necesita aflojar la cuerda"
        elif  frecuenciaDominante > 110.0 - tolerancia and frecuenciaDominante < 110.0 + tolerancia:
            Cuerda = "5ta La(A) 110.00 Hz"
            if  frecuenciaDominante > 110.0 - toleranciaAfinada and frecuenciaDominante < 110.0 + toleranciaAfinada:
                Afinacion = "La afinacion se oye bien"
            elif  frecuenciaDominante < 110.0 + toleranciaAfinada:
                Afinacion = "Se necesita apretar la cuerda"
            else:
                Afinacion = "Se necesita aflojar la cuerda"
        elif  frecuenciaDominante > 146.83 - tolerancia and frecuenciaDominante < 146.83 + tolerancia:
            Cuerda = "4ta Re(D) 146.83 Hz"
            if  frecuenciaDominante > 146.83 - toleranciaAfinada and frecuenciaDominante < 146.83 + toleranciaAfinada:
                Afinacion = "La afinacion se oye bien"
            elif  frecuenciaDominante < 146.83 + toleranciaAfinada:
                Afinacion = "Se necesita apretar la cuerda"
            else:
                Afinacion = "Se necesita aflojar la cuerda"
        elif  frecuenciaDominante > 196.0 - tolerancia and frecuenciaDominante < 196.0 + tolerancia:
            Cuerda = "3ra Sol(G) 196.0 Hz"
            if  frecuenciaDominante > 196.0 - toleranciaAfinada and frecuenciaDominante < 196.0 + toleranciaAfinada:
                Afinacion = "La afinacion se oye bien"
            elif  frecuenciaDominante < 196.0 + toleranciaAfinada:
                Afinacion = "Se necesita apretar la cuerda"
            else:
                Afinacion = "Se necesita aflojar la cuerda"
        elif  frecuenciaDominante > 246.94 - tolerancia and frecuenciaDominante < 246.94 + tolerancia:
            Cuerda = "2da Si(B) 246.94 Hz"
            if  frecuenciaDominante > 246.94 - toleranciaAfinada and frecuenciaDominante < 246.94 + toleranciaAfinada:
                Afinacion = "La afinacion se oye bien"
            elif  frecuenciaDominante < 246.94 + toleranciaAfinada:
                Afinacion = "Se necesita apretar la cuerda"
            else:
                Afinacion = "Se necesita aflojar la cuerda"
        elif  frecuenciaDominante > 329.63 - tolerancia and frecuenciaDominante < 329.63 + tolerancia:
            Cuerda = "1ra Mi(E2) 329.63 Hz"
            if  frecuenciaDominante > 329.63- toleranciaAfinada and frecuenciaDominante < 329.63 + toleranciaAfinada:
                Afinacion = "La afinacion se oye bien"
            elif  frecuenciaDominante < 329.63 + toleranciaAfinada:
                Afinacion = "Se necesita apretar la cuerda"
            else:
                Afinacion = "Se necesita aflojar la cuerda"
        else:
            Cuerda = "Cuerda no identificada"
            Afinacion = "Presione el botón 'Iniciar' otra vez"

        stringCuerda.set(Cuerda)
        stringFrecuenciaA.set(FrecuenciaActual)
        stringAfinacion.set(Afinacion)


    if __name__ == "__main__":
        p = pyaudio.PyAudio()
        stream = p.open(format = PROFUNDIDAD_BITS, channels = CANALES, rate = FRECUENCIA_MUESTREO, input = True, frames_per_buffer = CHUNK)

        for i in range(0, int(FRECUENCIA_MUESTREO * TIEMPO_GRABACION / CHUNK )):
            analizar(stream)

        stream.stop_stream()
        stream.close()
        p.terminate()







btnCalcular = Button(ventana, text = "Inicio", command = iniciar)
btnCalcular.pack()

laCuerda = Label(ventana, textvariable = stringCuerda)
laCuerda.pack()

frecuenciaA = Label(ventana, textvariable = stringFrecuenciaA)
frecuenciaA.pack()

frecuencia = Label(ventana, textvariable = stringFrecuencia)
frecuencia.pack()

afinacion = Label(ventana, textvariable = stringAfinacion)
afinacion.pack()

ventana.mainloop()
