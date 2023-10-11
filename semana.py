from datetime import date

class semana:

    id = 0
    dia = date(2023,10,11)
    temperatura = 0.0

    def __init__(self,id,dia,temperatura) -> None:
        self.id = id
        self.dia = dia
        self.temperatura = temperatura
