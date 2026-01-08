from conexion import supabase

class DPersona:
    def __init__(self):
        self.db = supabase
        self.tabla = "pacientes"

    def mostrarPersonas(self):
        res = self.db.table(self.tabla).select(
            "id, nombre, apellido, email, presupuesto"
        ).execute()
        return res.data if res.data else []

    def insertarPersona(self, persona):
        self.db.table(self.tabla).insert({
            "nombre": persona["nombre"],
            "apellido": persona["apellido"],
            "email": persona["email"],
            "presupuesto": persona["presupuesto"]
        }).execute()
        return True

    def eliminarPersona(self, id):
        self.db.table(self.tabla).delete().eq("id", id).execute()
        return True
