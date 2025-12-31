from capadatos.personas import DPersona

class LPersona:
    def __init__(self):
        self.dpersona = DPersona()

    def mostrarPersonas(self):
        return self.dpersona.mostrarPersonas()

    def insertarPersona(self, persona: dict):
        # Solo pasa el diccionario tal cual
        return self.dpersona.insertarPersona(persona)

    def actualizarPersona(self, persona: dict, id: int):
        return self.dpersona.actualizarPersona(persona, id)

    def eliminarPersona(self, id: int):
        return self.dpersona.eliminarPersona(id)
