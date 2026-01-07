from conexion import supabase

class DPersona:
    def __init__(self):
        self.__db = supabase
        self.__schema = "public"
        self.__nombreTabla = "empleados"
        self.__camposPermitidos = ["nombre", "apellidos", "salario"]

    def __ejecutarConsulta(self, consulta):
        try:
            return consulta.execute().data
        except Exception:
            return []

    def mostrarPersonas(self):
        consulta = (
            self.__db
            .schema(self.__schema)
            .table(self.__nombreTabla)
            .select("id, nombre, apellidos, salario")
        )
        return self.__ejecutarConsulta(consulta)

    def insertarPersona(self, persona):
        try:
            datos = {}
            for campo in self.__camposPermitidos:
                if campo in persona:
                    datos[campo] = persona[campo]

            if "nombre" in datos and "apellidos" in datos and "salario" in datos:
                (
                    self.__db
                    .schema(self.__schema)
                    .table(self.__nombreTabla)
                    .insert(datos)
                    .execute()
                )
                return True

            return False
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
