from capadatos.personas import DPersona

class LPersona:
    def __init__(self):
        self.dpersona = DPersona()

    def mostrarPersonas(self):
        return self.dpersona.mostrarPersonas()

    def insertarPersona(self, persona):
        if (
            persona.get("nombre") and
            persona.get("apellidos") and
            persona.get("email") and
            persona.get("salario", 0) >= 1000
        ):
            return self.dpersona.insertarPersona(persona)
        return False

    def eliminarPersona(self, id):
        return self.dpersona.eliminarPersona(id)
