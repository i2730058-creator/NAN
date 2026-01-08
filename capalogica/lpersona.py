from capadatos.personas import DPersona

class LPersona:
    def __init__(self):
        self.dpersona = DPersona()

    def mostrarPersonas(self):
        return self.dpersona.mostrarPersonas()

    def _nombre_valido(self, nombre):
        return nombre.replace(" ", "").isalpha()

    def _apellido_valido(self, apellido):
        return apellido.replace(" ", "").isalpha()

    def _email_valido(self, email):
        return "@" in email and "." in email

    def _presupuesto_valido(self, presupuesto):
        try:
            return float(presupuesto) >= 0
        except:
            return False

    def insertarPersona(self, persona):
        if not self._nombre_valido(persona["nombre"]):
            return False
        if not self._apellido_valido(persona["apellido"]):
            return False
        if not self._email_valido(persona["email"]):
            return False
        if not self._presupuesto_valido(persona["presupuesto"]):
            return False

        persona["presupuesto"] = float(persona["presupuesto"])
        return self.dpersona.insertarPersona(persona)

    def actualizarPersona(self, persona):
        if persona["id"] <= 0:
            return False
        return self.insertarPersona(persona) and self.dpersona.actualizarPersona(persona)

    def eliminarPersona(self, id):
        return id > 0 and self.dpersona.eliminarPersona(id)
