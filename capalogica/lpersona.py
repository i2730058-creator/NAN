from capadatos.personas import DPersona

class LPersona:
    def __init__(self):
        self.dpersona = DPersona()

    def mostrarPersonas(self):
        return self.dpersona.mostrarPersonas()

    def insertarPersona(self, persona):
        try:
            persona["salario"] = float(str(persona["salario"]).replace(",", "."))
            return self.dpersona.insertarPersona(persona)
        except Exception:
            return False

    def eliminarPersona(self, id):
        return self.dpersona.eliminarPersona(id)
