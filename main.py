import customtkinter as ctk
from datetime import date
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from semana import Semana

def mostrar_resultados():
    lbl_promedio.config(text=f"Promedio: {semana.calcular_promedio():.2f}°C")
    lbl_maximo.config(text=f"Máximo: {semana.temperatura_maxima()}°C")
    lbl_minimo.config(text=f"Mínimo: {semana.temperatura_minima()}°C")

def guardar_temperaturas():
    for dia, entrada in entradas.items():
        try:
            temperatura = float(entrada.get())
            semana.registrar_temperatura(dia, temperatura)
        except ValueError:
            pass
    mostrar_resultados()

def mostrar_grafico():
    dias = list(semana.temperaturas.keys())
    temps = [semana.temperaturas[dia] for dia in dias]
    
    fig, ax = plt.subplots()
    ax.plot(dias, temps, marker='o')
    ax.set_title('Temperaturas de la Semana')
    ax.set_xlabel('Día')
    ax.set_ylabel('Temperatura (°C)')
    
    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
    canvas.draw()


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
btn_guardar.grid(row=0, column=2, pady=10)

btn_grafico = ctk.CTkButton(ventana, text="Mostrar Gráfico", command=mostrar_grafico)
btn_grafico.grid(row=1, column=2, pady=10)

lbl_promedio = ctk.CTkLabel(ventana, text="Promedio: --°C")
lbl_promedio.grid(row=2, column=2)

lbl_maximo = ctk.CTkLabel(ventana, text="Máximo: --°C")
lbl_maximo.grid(row=3, column=2)

lbl_minimo = ctk.CTkLabel(ventana, text="Mínimo: --°C")
lbl_minimo.grid(row=4, column=2)

ventana.mainloop()