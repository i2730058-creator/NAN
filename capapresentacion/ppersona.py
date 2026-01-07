import streamlit as st
from capalogica.lpersona import LPersona

class PPersona:
    def __init__(self):
        self.lpersona = LPersona()
        self.construirInterfaz()

    def construirInterfaz(self):
        st.title("MOOVA CLINIC")

        with st.form("formulario_registro"):
            txtnombre = st.text_input("Nombre")
            txtapellidos = st.text_input("Apellidos")
            txtcorreo = st.text_input("Correo")
            txtsalario = st.number_input("Salario", min_value=1000.0)
            btnGuardar = st.form_submit_button("Guardar", type="primary")

        if btnGuardar:
            persona = {
                "nombre": txtnombre,
                "apellidos": txtapellidos,
                "correo": txtcorreo,
                "salario": float(txtsalario)
            }
            self.lpersona.insertarPersona(persona)

        st.dataframe(self.lpersona.mostrarPersonas())
