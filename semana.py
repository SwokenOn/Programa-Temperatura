from datetime import date
from typing import Any

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

    def id(self,id):
        self.id = id
    def id(self):
        return self.id
    
    def temperaturas(self,temperaturas):
        self.temperaturas = temperaturas
    def temperaturas(self):
        return self.temperaturas

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

    def temperatura_maxima(self):
        return max(filter(None, self.temperaturas.values()))

    def temperatura_minima(self):
        return min(filter(None, self.temperaturas.values()))