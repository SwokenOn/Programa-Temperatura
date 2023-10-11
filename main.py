import customtkinter as ctk
from datetime import date
import tkinter as tk
from semana import Semana

def guardar_temperaturas():
    for dia, entrada in entradas.items():
        try:
            temperatura = float(entrada.get())
            semana.registrar_temperatura(dia, temperatura)
        except ValueError:
            pass

ventana = ctk.CTk()
ventana.title("Registro de Temperaturas")
semana = Semana(date(2023, 10, 11))
entradas = {}


ventana.mainloop()