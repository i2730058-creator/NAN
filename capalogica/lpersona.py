import re
from capadatos.personas import DPersona

class LPersona:
    def __init__(self):
        self.dpersona = DPersona()

    def mostrarPersonas(self):
        return self.dpersona.mostrarPersonas()

    def _datos_validos(self, p):
        try:
            if p["salario"] < 1000:
                return False

            if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', p["correo"]):
                return False

            if not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$', p["nombre"]):
                return False

            if not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$', p["apellidos"]):
                return False

            return True
        except Exception:
            return False

    def insertarPersona(self, persona):
        if self._datos_validos(persona):
            return self.dpersona.insertarPersona(persona)
        return False

    def actualizarPersona(self, persona, id):
        if id > 0 and self._datos_validos(persona):
            return self.dpersona.actualizarPersona(persona, id)
        return False

    def eliminarPersona(self, id):
        if id > 0:
            return self.dpersona.eliminarPersona(id)
        return False
