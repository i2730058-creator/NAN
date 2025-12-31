import streamlit as st
from capalogica.LPersona import LPersona

class PPersona:
    def __init__(self):
        self.lpersona = LPersona()
        self.construirInterfaz()

    def construirInterfaz(self):
        st.title("MOOVA CLINIC")

        with st.form("formulario_registro"):
            txtnombre = st.text_input("Nombre")
            txtapellido = st.text_input("Apellido")
            txtemail = st.text_input("Email")
            txtfecha = st.date_input("Fecha de ingreso")
            txtsalario = st.number_input("Salario", min_value=0.0)
            btnGuardar = st.form_submit_button("Guardar", type="primary")

        if btnGuardar:
            persona = {
                "nombre": txtnombre,
                "apellido": txtapellido,
                "email": txtemail,
                "fecha_ingreso": txtfecha.isoformat(),
                "salario": txtsalario
            }

            resultado = self.lpersona.insertarPersona(persona)

            if hasattr(resultado, "data"):
                st.toast("Registro guardado correctamente")
                self.mostrarPersonas()
            else:
                st.error(f"Error al guardar: {resultado}")

    def mostrarPersonas(self):
        listaPersonas = self.lpersona.mostrarPersonas()

        if isinstance(listaPersonas, list):
            if len(listaPersonas) > 0:
                st.dataframe(listaPersonas)
            else:
                st.warning("No hay registros.")
        else:
            st.error(f"Error al obtener los datos: {listaPersonas}")
