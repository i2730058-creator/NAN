from conexion import supabase

class DPersona:
    def __init__(self):
        self.db = supabase
        self.tabla = "pacientes"

    def mostrarPersonas(self):
        try:
            res = self.db.table(self.tabla).select(
                "id, nombre, apellido, email, presupuesto"
            ).execute()
            return res.data
        except Exception:
            return []

    def insertarPersona(self, persona: dict):
        try:
            self.db.table(self.tabla).insert({
                "nombre": persona["nombre"],
                "apellido": persona["apellido"],
                "email": persona["email"],
                "presupuesto": persona["presupuesto"]
            }).execute()
            return True
        except Exception:
            return False

    def actualizarPersona(self, persona: dict):
        try:
            self.db.table(self.tabla).update({
                "nombre": persona["nombre"],
                "apellido": persona["apellido"],
                "email": persona["email"],
                "presupuesto": persona["presupuesto"]
            }).eq("id", persona["id"]).execute()
            return True
        except Exception:
            return False

    def eliminarPersona(self, id: int):
        try:
            self.db.table(self.tabla).delete().eq("id", id).execute()
            return True
        except Exception:
            return False
