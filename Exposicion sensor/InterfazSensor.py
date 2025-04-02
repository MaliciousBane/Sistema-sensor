import tkinter as tk
from Sensor import Sensor
class Interfaz:
    def __init__(self):
        self.ventana_formulario = tk.Tk()
        self.ventana_formulario.title("Sistema Sensor")
        self.objSensor = Sensor()

        self.label_Temperatura = tk.Label(self.ventana_formulario, text="Temperatura: ")
        self.label_Temperatura.configure(bg="yellow", fg = "red")
        self.label_mostrar_temperatura = tk.Label(self.ventana_formulario, text= self.objSensor.mostrar_dato_temperatura )
        self.label_mostrar_temperatura.configure(bg="yellow", fg = "red")

        self.label_humedad = tk.Label(self.ventana_formulario, text="Humedad: ")
        self.label_humedad.configure(bg="yellow", fg = "red")
        self.label_mostrar_humedad = tk.Label(self.ventana_formulario, text= self.objSensor.mostrar_dato_humedad )
        self.label_mostrar_humedad.configure(bg="yellow", fg = "red")

        self.label_umbral = tk.Label(self.ventana_formulario, text="Ingrese umbral de temperatura: ")
        self.label_umbral.configure(bg="yellow", fg = "red")
        self.entry_umbral = tk.Entry(self.ventana_formulario)

        self.label_alerta = tk.Label(self.ventana_formulario, text="Estado", foreground= lambda : self.cambio_estado())

        self.boton_enviar = tk.Button(self.ventana_formulario, text="Enviar", command= lambda : self.tomar_datos())
        self.boton_enviar.configure(bg="blue", fg="yellow", width=30)
        self.boton_historial = tk.Button(self.ventana_formulario, text="Mostrar Historial", command= lambda : self.evento_historial())
        self.boton_historial.configure(bg="blue", fg="yellow", width=30)

        self.label_Temperatura.grid(row=0, column=0)
        self.label_mostrar_temperatura.grid(row=0, column=1)
        self.label_humedad.grid(row=1, column=0)
        self.label_mostrar_humedad.grid(row=1, column=1)
        self.boton_enviar.grid(row=2, column=0)
        self.boton_historial.grid(row=2, column=1)