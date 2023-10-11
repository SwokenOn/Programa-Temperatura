from datetime import date

class Semana:
    id = date(2023, 10, 11)
    temperaturas = {
        "Lunes": None,
        "Martes": None,
        "Miércoles": None,
        "Jueves": None,
        "Viernes": None,
        "Sábado": None,
        "Domingo": None
    }

    def __init__(self, id):
        self.id = id
    
    def __init__(self, id):
        self.id = id

    def registrar_temperatura(self, dia, temperatura):
        if dia in self.temperaturas:
            self.temperaturas[dia] = temperatura
        else:
            print("Día no válido.")

    def calcular_promedio(self):
        total = 0
        dias_contados = 0
        for temp in self.temperaturas.values():
            if temp is not None:
                total += temp
                dias_contados += 1
        return total / dias_contados if dias_contados > 0 else 0
