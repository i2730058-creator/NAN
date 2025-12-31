from capadatos.DPersona import DPersona

class LPersona:
    def __init__(self):
        self.__dpersona = DPersona()

    def mostrarPersonas(self):
        return self.__dpersona.mostrarPersonas()

    def insertarPersona(self, persona: dict):
        return self.__dpersona.insertarPersona(persona)

    def actualizarPersona(self, persona: dict, docidentidad: str):
        return self.__dpersona.actualizarPersona(persona, docidentidad)

    def eliminarPersona(self, docidentidad: str):
        return self.__dpersona.eliminarPersona(docidentidad)
