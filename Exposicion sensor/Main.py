from InterfazSensor import Interfaz

class Main:
    def __init__(self):
        self.objFormulario = Interfaz()

    def ejecutar(self):
        auxFormulario = self.objFormulario.iniciar_ventana()
        auxFormulario.mainloop()

if __name__ == "__main__":
    app = Main()
    app.ejecutar()
