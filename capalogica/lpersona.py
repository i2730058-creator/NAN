import re
from capadatos.personas import DPersona

class LPersona:
    def __init__(self):
        self.dpersona = DPersona()

    def mostrarPersonas(self):
        return self.dpersona.mostrarPersonas()

    def _datos_validos(self, p):
        try:
            return (
                p["salario"] >= 1000
                and re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', p["correo"])
                and re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$', p["nombre"])
                and re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$', p["apellidos"])
            )
        except Exception:
            return False

    def insertarPersona(self, persona):
        return self._datos_validos(persona) and self.dpersona.insertarPersona(persona)

    def actualizarPersona(self, persona, id):
        return id > 0 and self._datos_validos(persona) and self.dpersona.actualizarPersona(persona, id)

    def eliminarPersona(self, id):
        return id > 0 and self.dpersona.eliminarPersona(id)
