from capadatos.personas import DPersona

class LPersona:
    def __init__(self):
        self.dpersona = DPersona()
        self.persona = None

    def mostrarPersonas(self):
        return self.dpersona.mostrarPersonas()

    def insertarPersona(self, persona: dict):
        return self.dpersona.insertarPersona(persona)

    def actualizarPersona(self, persona: dict, docidentidad: str):
        return self.dpersona.actualizarPersona(persona, docidentidad)

    def eliminarPersona(self, docidentidad: str):
        return self.dpersona.eliminarPersona(docidentidad)

    def setPersona(self, persona: dict):
        self.persona = persona
