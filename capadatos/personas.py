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
        # Solo insertamos las columnas que existen
        consulta = self.__db.table(self.__nombreTabla).insert(persona)
        return self.__ejecutarConsulta(consulta)

    def actualizarPersona(self, persona: dict, id: int):
        consulta = self.__db.table(self.__nombreTabla).update(persona).eq("id", id)
        return self.__ejecutarConsulta(consulta)

    def eliminarPersona(self, id: int):
        consulta = self.__db.table(self.__nombreTabla).delete().eq("id", id)
        return self.__ejecutarConsulta(consulta)
