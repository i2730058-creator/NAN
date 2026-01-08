from capadatos.personas import DPersona

class LPersona:
    def __init__(self):
        self.__capadatos = DPersona()

    def nuevaPersona(self, persona: dict):
        if not self._datosCompletos(persona):
            return False

        return self.__capadatos.insertarPersona(persona)

    def mostrarPersonas(self):
        return self.__capadatos.mostrarPersonas()

    def actualizarPersona(self, persona: dict):
        if "id" not in persona:
            return False

        if not self._datosCompletos(persona):
            return False

        return self.__capadatos.actualizarPersona(persona)

    def eliminarPersona(self, id: int):
        if id <= 0:
            return False

        return self.__capadatos.eliminarPersona(id)

    def _datosCompletos(self, persona: dict):
        try:
            return (
                persona["nombre"] != "" and
                persona["apellido"] != "" and
                persona["email"] != "" and
                persona["presupuesto"] != ""
            )
        except Exception:
            return False
