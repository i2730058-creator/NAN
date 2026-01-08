from capadatos.personas import DPersona

class LPersona:
    def __init__(self):
        self.dpersona = DPersona()

    def mostrarPersonas(self):
        return self.dpersona.mostrarPersonas()

    def insertarPersona(self, persona):
        if not persona["nombre"]:
            return False
        if not persona["apellido"]:
            return False
        if not persona["email"]:
            return False
        if persona["presupuesto"] < 0:
            return False

        return self.dpersona.insertarPersona(persona)

    def eliminarPersona(self, id):
        if id <= 0:
            return False
        return self.dpersona.eliminarPersona(id)
