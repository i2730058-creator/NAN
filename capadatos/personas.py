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
            datos = {
                "nombre": persona.get("nombre", ""),
                "apellido": persona.get("apellido", ""),
                "email": persona.get("email", ""),
                "salario": float(persona.get("salario", 0))
            }
            self.__db.table(self.__nombreTabla).schema(self.__schema).insert(datos).execute()
            return True
        except Exception:
            return False

    def eliminarPersona(self, id):
        try:
            self.__db.table(self.__nombreTabla).schema(self.__schema).delete().eq("id", id).execute()
            return True
        except Exception:
            return False
