import tkinter as tk
from Sensor import Sensor

class Interfaz:
    def __init__(self):
        self.ventana_formulario = tk.Tk()
        self.ventana_formulario.title("Sistema Sensor")
        self.objSensor = Sensor()
        self.historial = []

        # Colores y fuentes
        bg_color = "#f0f8ff"
        label_font = ("Arial", 11)
        title_font = ("Arial", 12, "bold")
        entry_font = ("Arial", 11)

        self.ventana_formulario.configure(bg=bg_color)

        self.label_Temperatura = tk.Label(self.ventana_formulario, text="Temperatura:", font=label_font, bg=bg_color)
        self.label_mostrar_temperatura = tk.Label(self.ventana_formulario, text="0 °C", font=title_font, bg="white", relief="sunken", width=10)

        self.label_humedad = tk.Label(self.ventana_formulario, text="Humedad:", font=label_font, bg=bg_color)
        self.label_mostrar_humedad = tk.Label(self.ventana_formulario, text="0 %", font=title_font, bg="white", relief="sunken", width=10)

        self.label_umbral = tk.Label(self.ventana_formulario, text="Ingrese umbral de temperatura:", font=label_font, bg=bg_color)
        self.entry_umbral = tk.Entry(self.ventana_formulario, font=entry_font)

        self.label_alerta = tk.Label(self.ventana_formulario, text="Estado", font=title_font, fg="black", bg=bg_color)

        self.boton_enviar = tk.Button(self.ventana_formulario, text="Enviar", command=self.tomar_datos, bg="#add8e6", font=label_font, width=15)
        self.boton_historial = tk.Button(self.ventana_formulario, text="Mostrar Historial", command=self.evento_historial, bg="#90ee90", font=label_font, width=15)

        # Layout
        self.label_Temperatura.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.label_mostrar_temperatura.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.label_humedad.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.label_mostrar_humedad.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.label_umbral.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_umbral.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.boton_enviar.grid(row=3, column=0, padx=10, pady=10)
        self.boton_historial.grid(row=3, column=1, padx=10, pady=10)

        self.label_alerta.grid(row=4, column=0, columnspan=2, sticky="ew", pady=10)

    def iniciar_ventana(self):
        self.ventana_formulario.geometry("400x230")
        self.ventana_formulario.resizable(False, False)
        return self.ventana_formulario

    def tomar_datos(self):
        try:
            umbral = float(self.entry_umbral.get())
            self.historial.append(umbral)

            self.objSensor.numero_aleatorio()
            temperatura = self.objSensor.mostrar_dato_temperatura()
            humedad = self.objSensor.mostrar_dato_humedad()

            self.label_mostrar_temperatura.config(text=f"{temperatura} °C")
            self.label_mostrar_humedad.config(text=f"{humedad} %")

            if temperatura > umbral:
                self.label_alerta.config(text="¡ALERTA!", fg="red")
            else:
                self.label_alerta.config(text="Normal", fg="green")
        except ValueError:
            self.label_alerta.config(text="Error: Ingrese un número válido", fg="orange")
        finally:
            self.entry_umbral.delete(0, 'end')

    def evento_historial(self):
        historial_texto = ""
        for temp in self.historial:
            historial_texto += str(temp) + "\n"
        ventana_historial = tk.Toplevel(self.ventana_formulario)
        ventana_historial.title("Historial de Umbrales")
        ventana_historial.configure(bg="#e6f2ff")
        tk.Label(ventana_historial, text=historial_texto, font=("Arial", 11), bg="#e6f2ff").pack(padx=15, pady=15)
