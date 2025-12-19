from CAPADATOS.personas import DPersona

class LPersona:
    def __init__(self):
        self.dpersona = DPersona()
        self.persona = None

    def __ejecutarconsultas(self, consulta, tipoconsulta=None):
        try:
            resultado = consulta.execute().data
            return resultado
        except Exception as e:
            return f'error : {e}'

    def mostrarPersonas(self):
        return self.dpersona.mostrarPersonas()

    def insertarpersona(self, persona: dict):
        return self.dpersona.insertarpersona(persona)

    def actualizarpersona(self, persona: dict, docidentidad: str):
        return self.dpersona.actualizarpersona(persona, docidentidad)

    def eliminarpersona(self, docidentidad: str):
        return self.dpersona.eliminarPersona(docidentidad)

    def setPersona(self, persona: dict):
        self.persona = persona
