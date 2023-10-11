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
for index, dia in enumerate(semana.temperaturas):
    label = ctk.CTkLabel(ventana, text=dia)
    label.grid(row=index, column=0, padx=10, pady=5)
    entrada = ctk.CTkEntry(ventana)
    entrada.grid(row=index, column=1, padx=10, pady=5)
    entradas[dia] = entrada

btn_guardar = ctk.CTkButton(ventana, text="Guardar", command=guardar_temperaturas)
btn_guardar.grid(row=len(semana.temperaturas), column=0, columnspan=2, pady=10)
ventana.mainloop()