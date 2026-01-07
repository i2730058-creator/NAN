import streamlit as st
from capalogica.lpersona import LPersona

class PPersona:
    def __init__(self):
        self.lpersona = LPersona()
        self.construir()

    def construir(self):
        st.title("Registro de Empleados")

        with st.form("form_registro"):
            nombre = st.text_input("Nombre")
            apellido = st.text_input("Apellido (puede ser dos palabras)")
            email = st.text_input("Correo electrónico")
            salario = st.text_input("Salario")
            guardar = st.form_submit_button("Guardar")

        if guardar:
            persona = {
                "nombre": nombre.strip(),
                "apellido": apellido.strip(),
                "email": email.strip(),
                "salario": salario.strip()
            }

            if self.lpersona.insertarPersona(persona):
                st.success("Registro guardado correctamente")
                st.rerun()
            else:
                st.error("No se pudo guardar el registro")

        st.subheader("Tabla de Empleados")
        datos = self.lpersona.mostrarPersonas()
        st.dataframe(datos, use_container_width=True)
