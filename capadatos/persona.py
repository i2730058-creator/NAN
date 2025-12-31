from conexion import supabase

class DPersona:
    def __init__(self):
        self.__db = supabase
        self.__nombreTabla = "empleados"

    def __ejecutarConsulta(self, consulta):
        try:
            resultado = consulta.execute().data
            return resultado
        except Exception as e:
            return f"Error: {e}"

    def mostrarPersonas(self):
        consulta = self.__db.table(self.__nombreTabla).select("*")
        return self.__ejecutarConsulta(consulta)

    def insertarPersona(self, persona: dict):
        respuesta = self.__db.table(self.__nombreTabla).insert(persona).execute()
        return respuesta

    def actualizarPersona(self, persona: dict, docidentidad: str):
        consulta = (
            self.__db
            .table(self.__nombreTabla)
            .update(persona)
            .eq("docidentidad", docidentidad)
        )
        return self.__ejecutarConsulta(consulta)

    def eliminarPersona(self, docidentidad: str):
        consulta = (
            self.__db
            .table(self.__nombreTabla)
            .delete()
            .eq("docidentidad", docidentidad)
        )
        return self.__ejecutarConsulta(consulta)
