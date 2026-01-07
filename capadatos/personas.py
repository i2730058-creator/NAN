from conexion import supabase

class DPersona:
    def __init__(self):
        self.__db = supabase
        self.__schema = "public"
        self.__nombreTabla = "empleados"

    def mostrarPersonas(self):
        try:
            return (
                self.__db
                .schema(self.__schema)
                .table(self.__nombreTabla)
                .select("*")
                .execute()
                .data
            )
        except Exception:
            return []

    def insertarPersona(self, persona):
        try:
            datos = {
                "nombre": str(persona.get("nombre", "")),
                "apellido": str(persona.get("apellido", "")),
                "email": str(persona.get("email", "")),
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
