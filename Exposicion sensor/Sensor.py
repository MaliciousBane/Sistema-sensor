import random

class Sensor:
    def __init__(self):
        self.temperatura = 0
        self.humedad = 0

    def numero_aleatorio(self):
        try:
            self.temperatura = abs(random.randint(0, 50))
            self.humedad = abs(random.randint(20, 90))
        except Exception as e:
            print("Error al generar los datos del sensor:", e)
        finally:
            pass  # Aquí puedes cerrar conexiones si fueran necesarias

    def mostrar_dato_humedad(self):
        return self.humedad

    def mostrar_dato_temperatura(self):
        return self.temperatura
