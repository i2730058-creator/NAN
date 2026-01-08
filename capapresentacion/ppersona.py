import streamlit as st
from capalogica.lpersona import LPersona

class PPersona:
    def __init__(self):
        self.lpersona = LPersona()
        self.construir()

    def construir(self):
        st.title("Registro de Pacientes")

        with st.form("form_registro"):
            nombre = st.text_input("Nombre")
            apellido = st.text_input("Apellido (puede ser dos palabras)")
            email = st.text_input("Correo electrónico")
            presupuesto = st.text_input("Presupuesto")
            guardar = st.form_submit_button("Guardar")

        if guardar:
            persona = {
                "nombre": nombre,
                "apellido": apellido,
                "email": email,
                "presupuesto": presupuesto
            }

            if self.lpersona.nuevaPersona(persona):
                st.success("Registro guardado correctamente")
                st.rerun()
            else:
                st.error("No se pudo guardar el registro")

        st.subheader("Tabla de Pacientes")
        datos = self.lpersona.mostrarPersona()
        st.dataframe(datos, use_container_width=True)
