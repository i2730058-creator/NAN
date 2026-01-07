from conexion import supabase

class DPersona:
    def __init__(self):
        self.db = supabase
        self.tabla = "empleados"

    def mostrarPersonas(self):
        try:
            res = self.db.table(self.tabla).select(
                "id, nombre, apellido, email, salario"
            ).execute()
            return res.data
        except Exception:
            return []

    def insertarPersona(self, persona):
        try:
            self.db.table(self.tabla).insert({
                "nombre": persona["nombre"],
                "apellido": persona["apellido"],
                "email": persona["email"],
                "salario": persona["salario"]
            }).execute()
            return True
        except Exception:
            return False

    def eliminarPersona(self, id):
        try:
            self.db.table(self.tabla).delete().eq("id", id).execute()
            return True
        except Exception:
            return False
