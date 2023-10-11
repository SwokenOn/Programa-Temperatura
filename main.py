import customtkinter
from datetime import date
import tkinter

def guardar_temperaturas():
    for dia, entrada in entradas.items():
        try:
            temperatura = float(entrada.get())
            semana.registrar_temperatura(dia, temperatura)
        except ValueError:
            pass

ventana = customtkinter.CTk()



ventana.mainloop()