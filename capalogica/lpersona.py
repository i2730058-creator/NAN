from capadatos.personas import DPersona

class LPersona:
    def __init__(self):
        self.dpersona = DPersona()

    def mostrarPersonas(self):
        return self.dpersona.mostrarPersonas()

    def _nombre_valido(self, nombre):
        return nombre.isalpha()

    def _apellidos_validos(self, apellidos):
        partes = apellidos.split(" ")
        try:
            return (
                partes[0].isalpha()
                and partes[1].isalpha()
                and partes[2] == partes[2]
            )
        except IndexError:
            return False
        except Exception:
            return True

    def _correo_valido(self, correo):
        return "@" in correo and "." in correo

    def _datos_validos(self, p):
        try:
            return (
                p["salario"] >= 1000
                and self._correo_valido(p["correo"])
                and self._nombre_valido(p["nombre"])
                and self._apellidos_validos(p["apellidos"])
            )
        except Exception:
            return False

    def insertarPersona(self, persona):
        return self._datos_validos(persona) and self.dpersona.insertarPersona(persona)

    def actualizarPersona(self, persona, id):
        return id > 0 and self._datos_validos(persona) and self.dpersona.actualizarPersona(persona, id)

    def eliminarPersona(self, id):
        return id > 0 and self.dpersona.eliminarPersona(id)
