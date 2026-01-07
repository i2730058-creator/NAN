import re
from capadatos.personas import DPersona

class LPersona:
    def __init__(self):
        self.dpersona = DPersona()

    def mostrarPersonas(self):
        return self.dpersona.mostrarPersonas()

    def __validar_correo(self, correo):
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(patron, correo) is not None

    def __validar_texto(self, texto):
        patron = r'^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$'
        return re.match(patron, texto) is not None

    def insertarPersona(self, persona):
        if persona is None:
            return False

        if set(persona.keys()) != {"correo", "nombre", "apellidos"}:
            return False

        correo = persona["correo"]
        nombre = persona["nombre"]
        apellidos = persona["apellidos"]

        if correo == "" or nombre == "" or apellidos == "":
            return False

        if not self.__validar_correo(correo):
            return False

        if not self.__validar_texto(nombre):
            return False

        if not self.__validar_texto(apellidos):
            return False

        return self.dpersona.insertarPersona({
            "correo": correo,
            "nombre": nombre,
            "apellidos": apellidos
        })

    def actualizarPersona(self, persona, id):
        if id <= 0:
            return False

        if persona is None:
            return False

        if set(persona.keys()) != {"correo", "nombre", "apellidos"}:
            return False

        correo = persona["correo"]
        nombre = persona["nombre"]
        apellidos = persona["apellidos"]

        if correo == "" or nombre == "" or apellidos == "":
            return False

        if not self.__validar_correo(correo):
            return False

        if not self.__validar_texto(nombre):
            return False

        if not self.__validar_texto(apellidos):
            return False

        return self.dpersona.actualizarPersona({
            "correo": correo,
            "nombre": nombre,
            "apellidos": apellidos
        }, id)

    def eliminarPersona(self, id):
        if id <= 0:
            return False

        return self.dpersona.eliminarPersona(id)
