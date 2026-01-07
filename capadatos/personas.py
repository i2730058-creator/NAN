from conexion import supabase

class DPersona:
    def __init__(self):
        self.__db = supabase
        self.__nombreTabla = "empleados"
        self.__camposPermitidos = {"correo", "nombre", "apellidos"}

    def __ejecutarConsulta(self, consulta):
        try:
            resultado = consulta.execute()
            return resultado.data if resultado.data else []
        except Exception:
            return []

    def mostrarPersonas(self):
        consulta = self.__db.table(self.__nombreTabla).select("id, correo, nombre, apellidos")
        return self.__ejecutarConsulta(consulta)

    def insertarPersona(self, persona: dict):
        try:
            datos_limpios = {
                clave: persona[clave]
                for clave in persona
                if clave in self.__camposPermitidos
            }

            if len(datos_limpios) != 3:
                return False

            self.__db.table(self.__nombreTabla).insert(datos_limpios).execute()
            return True
        except Exception:
            return False

    def actualizarPersona(self, persona: dict, id: int):
        try:
            datos_limpios = {
                clave: persona[clave]
                for clave in persona
                if clave in self.__camposPermitidos
            }

            if not datos_limpios:
                return False

            consulta = (
                self.__db
                .table(self.__nombreTabla)
                .update(datos_limpios)
                .eq("id", id)
            )
            self.__ejecutarConsulta(consulta)
            return True
        except Exception:
            return False

    def eliminarPersona(self, id: int):
        consulta = self.__db.table(self.__nombreTabla).delete().eq("id", id)
        return self.__ejecutarConsulta(consulta)
