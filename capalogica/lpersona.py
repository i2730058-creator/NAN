from capadatos.personas import DPersona

class LPersona:
    def __init__(self):
        self.dpersona = DPersona()

    def mostrarPersonas(self):
        return self.dpersona.mostrarPersonas()

    def insertarPersona(self, persona):
        # Validación simple: que no estén vacíos los campos obligatorios
        if persona.get("nombre") and persona.get("apellido") and persona.get("email"):
            return self.dpersona.insertarPersona(persona)
        return False

    def eliminarPersona(self, id):
        return self.dpersona.eliminarPersona(id)
