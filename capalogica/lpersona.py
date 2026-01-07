from capadatos.personas import DPersona

class LPersona:
    def __init__(self):
        self.dpersona = DPersona()

    def mostrarPersonas(self):
        return self.dpersona.mostrarPersonas()

    def insertarPersona(self, persona):
        # Solo verificar que los campos obligatorios no estén vacíos
        if persona.get("nombre") != "" and persona.get("apellido") != "" and persona.get("email") != "":
            return self.dpersona.insertarPersona(persona)
        return False

    def eliminarPersona(self, id):
        return self.dpersona.eliminarPersona(id)
