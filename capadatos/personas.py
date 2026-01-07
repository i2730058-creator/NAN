from conexion import supabase

class DPersona:
    def __init__(self):
        self.__db = supabase
        self.__schema = "public"
        self.__nombreTabla = "empleados"

    def __ejecutarConsulta(self, consulta):
        try:
            return consulta.execute().data
        except Exception:
            return []

    def mostrarPersonas(self):
        return (
            self.__db
            .schema(self.__schema)
            .table(self.__nombreTabla)
            .select("*")
            .execute()
            .data
        )

    def insertarPersona(self, persona):
        try:
            (
                self.__db
                .schema(self.__schema)
                .table(self.__nombreTabla)
                .insert(persona)
                .execute()
            )
            return True
        except Exception:
            return False

    def eliminarPersona(self, id):
        try:
            (
                self.__db
                .schema(self.__schema)
                .table(self.__nombreTabla)
                .delete()
                .eq("id", id)
                .execute()
            )
            return True
        except Exception:
            return False
