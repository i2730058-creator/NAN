import streamlit as st
from capalogica.LPersona import LPersona

class PPersona:
    def __init__(self):
        self.lpersona = LPersona()
        self.construirInterfaz()

    def construirInterfaz(self):
        st.title("MOOVA CLINIC")

        with st.form("formulario_registro"):
            txtdocidentidad = st.text_input("Documento de identidad")
            txtnombre = st.text_input("Nombre")
            txtedad = st.number_input("Edad", min_value=0, step=1)
            btnGuardar = st.form_submit_button("Guardar", type="primary")

        if btnGuardar:
            persona = {
                "docidentidad": txtdocidentidad,
                "nombre": txtnombre,
                "edad": txtedad
            }

            resultado = self.lpersona.insertarPersona(persona)

            if isinstance(resultado, list):
                st.toast("Registro guardado correctamente", icon="👌")
                self.mostrarPersonas()
            else:
                st.error(f"Error al guardar: {resultado}")

    def mostrarPersonas(self):
        listaPersonas = self.lpersona.mostrarPersonas()

        if isinstance(listaPersonas, list):
            if len(listaPersonas) > 0:
                st.dataframe(listaPersonas)
            else:
                st.warning("No hay personas registradas.")
        else:
            st.error(f"Error al obtener los datos: {listaPersonas}")
