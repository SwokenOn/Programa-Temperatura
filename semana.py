from datetime import date

class semana:

    id = date(2023,10,11)
    dia = ""
    temperatura = 0.0

    def __init__(self,id,dia,temperatura) -> None:
        self.id = id
        self.dia = dia
        self.temperatura = temperatura
    
    def Calcular_Promedio(te):
