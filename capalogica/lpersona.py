from capadatos.personas import DPersona

class LPersona:
    __capadatos: DPersona

    def __init__(self):
        self.__capadatos = DPersona()

    def nuevaPersona(self, persona: dict):
        if not self._nombre_valido(persona["nombre"]):
            return False

        if not self._apellido_valido(persona["apellido"]):
            return False

        if not self._email_valido(persona["email"]):
            return False

        if not self._presupuesto_valido(persona["presupuesto"]):
            return False

        persona["presupuesto"] = float(persona["presupuesto"])
        return self.__capadatos.insertarPersona(persona)

    def mostrarPersona(self):
        return self.__capadatos.mostrarPersonas()

    def actualizarPersona(self, persona: dict, id: int):
        return self.__capadatos.actualizarPersona(persona, id)

    def eliminarPersona(self, id: int):
        return self.__capadatos.eliminarPersona(id)

    def _nombre_valido(self, nombre):
        return nombre.replace(" ", "").isalpha()

    def _apellido_valido(self, apellido):
        partes = apellido.split(" ")
        for p in partes:
            if p == "" or not p.isalpha():
                return False
        return True

    def _email_valido(self, email):
        return "@" in email and "." in email

    def _presupuesto_valido(self, presupuesto):
        try:
            return float(presupuesto) >= 0
        except:
            return False
