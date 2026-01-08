import streamlit as st
from capalogica.lpersona import LPersona

class PPersona:
    def __init__(self):
        self.lpersona = LPersona()
        self.construir()

    def construir(self):

        st.set_page_config(layout="wide")
        st.title("Registro de Pacientes")

        with st.form("form_registro"):
            nombre = st.text_input("Nombre")
            apellido = st.text_input("Apellido (puede ser dos palabras)")
            email = st.text_input("Correo electrónico")
            presupuesto = st.number_input("Presupuesto", min_value=0.0)
            guardar = st.form_submit_button("Guardar")

        if guardar:
            if (
                nombre == "" or
                apellido == "" or
                email == "" or
                presupuesto <= 0
            ):
                st.warning("Complete todos los campos correctamente")
            else:
                persona = {
                    "nombre": nombre,
                    "apellido": apellido,
                    "email": email,
                    "presupuesto": presupuesto
                }

                if self.lpersona.insertarPersona(persona):
                    st.success("Paciente registrado")
                    st.rerun()
                else:
                    st.error("No se pudo registrar")

        st.divider()

        st.subheader("Buscar paciente")
        filtro = st.text_input("Buscar por nombre, apellido o correo")

        datos = self.lpersona.mostrarPersonas()

        if filtro != "":
            datos = [
                p for p in datos
                if filtro.lower() in p["nombre"].lower()
                or filtro.lower() in p["apellido"].lower()
                or filtro.lower() in p["email"].lower()
            ]

        st.subheader("Listado de pacientes")
        st.dataframe(datos, use_container_width=True)
