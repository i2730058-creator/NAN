from conexion import supabase

class DPersona:
    def __init__(self):
        self.__db = supabase
        self.__nombreTabla = "empleados"

    def __ejecutarConsulta(self, consulta):
        try:
            resultado = consulta.execute()
            return resultado.data if resultado.data else []
        except Exception:
            return []

    def mostrarPersonas(self):
        consulta = self.__db.table(self.__nombreTabla).select("*")
        return self.__ejecutarConsulta(consulta)

    def insertarPersona(self, persona: dict):
        try:
            self.__db.table(self.__nombreTabla).insert(persona).execute()
            return True
        except Exception:
            return False

    def actualizarPersona(self, persona: dict, id: int):
        consulta = self.__db.table(self.__nombreTabla).update(persona).eq("id", id)
        return self.__ejecutarConsulta(consulta)

    def eliminarPersona(self, id: int):
        consulta = self.__db.table(self.__nombreTabla).delete().eq("id", id)
        return self.__ejecutarConsulta(consulta)
