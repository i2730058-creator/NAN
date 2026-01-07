from capadatos.personas import DPersona

class LPersona:
    def __init__(self):
        self.dpersona = DPersona()

    def mostrarPersonas(self):
        return self.dpersona.mostrarPersonas()

    def _nombre_valido(self, nombre):
        return nombre.replace(" ", "").isalpha()

    def _apellido_valido(self, apellido):
        partes = apellido.split(" ")
        if len(partes) < 1:
            return False
        for p in partes:
            if not p.isalpha():
                return False
        return True

    def _email_valido(self, email):
        return "@" in email and "." in email

    def _salario_valido(self, salario):
        try:
            return float(salario) >= 0
        except:
            return False

    def insertarPersona(self, persona):
        if not self._nombre_valido(persona["nombre"]):
            return False

        if not self._apellido_valido(persona["apellido"]):
            return False

        if not self._email_valido(persona["email"]):
            return False

        if not self._salario_valido(persona["salario"]):
            return False

        persona["salario"] = float(persona["salario"])
        return self.dpersona.insertarPersona(persona)

    def eliminarPersona(self, id):
        return id > 0 and self.dpersona.eliminarPersona(id)
