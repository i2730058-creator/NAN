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
            btnGuardar = st.form_submit_button("Guardar", type="primary")

        if btnGuardar:
            if txtnombre == "" or txtapellidos == "" or txtcorreo == "":
                st.warning("Todos los campos son obligatorios")
            else:
                persona = {
                    "correo": txtcorreo,
                    "nombre": txtnombre,
                    "apellidos": txtapellidos
                }

                resultado = self.lpersona.insertarPersona(persona)

                if resultado:
                    st.success("Registro guardado correctamente")
                else:
                    st.error("Datos inválidos. Verifique la información ingresada.")

        self.mostrarPersonas()

    def mostrarPersonas(self):
        listaPersonas = self.lpersona.mostrarPersonas()

        if listaPersonas and len(listaPersonas) > 0:
            st.dataframe(listaPersonas)
        else:
            st.info("No hay registros para mostrar.")
