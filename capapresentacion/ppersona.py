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
            txtapellido = st.text_input("Apellido")
            txtemail = st.text_input("Email")
            txtsalario = st.number_input("Salario", min_value=0.0)
            btnGuardar = st.form_submit_button("Guardar", type="primary")

        if btnGuardar:
            # Validaciones
            if not txtnombre.strip() or not txtapellido.strip():
                st.error("Nombre y apellido son obligatorios")
                return

            # Preparar datos para insertar
            persona = {
                "nombre": txtnombre.strip(),
                "apellido": txtapellido.strip(),
                "email": txtemail.strip() if txtemail else None,
                "salario": float(txtsalario)
            }

            # Insertar en Supabase
            try:
                resultado = self.lpersona.insertarPersona(persona)
                if hasattr(resultado, "data"):
                    st.toast("Registro guardado correctamente")
                    self.mostrarPersonas()
                else:
                    st.error(f"Error al guardar: {resultado}")
            except Exception as e:
                st.error(f"Error al guardar en Supabase: {e}")

    def mostrarPersonas(self):
        listaPersonas = self.lpersona.mostrarPersonas()

        if isinstance(listaPersonas, list):
            if len(listaPersonas) > 0:
                st.dataframe(listaPersonas)
            else:
                st.warning("No hay registros.")
        else:
            st.error(f"Error al obtener los datos: {listaPersonas}")
