import random
class Sensor:
    def __init__(self):
        self.temperatura = 0
        self.humedad = 0

    def numero_aleatorio(self):
        self.temperatura = random.randint(0,50)
        self.humedad =  random.randint(20,90)

    def mostrar_dato_humedad(self):
        return self.humedad
    
    def mostrar_dato_temperatura(self):
        return self.temperatura