import streamlit as st
from capalogica.lpersona import LPersona

class PPersona:
    def __init__(self):
        self.lpersona = LPersona()
        self.construir()

    def construir(self):
        st.markdown(
            """
            <style>
            .stApp {
                background-color: white;
            }

            h1, h2 {
                color: #1CA3EC;
            }

            button[kind="primary"] {
                background-color: #1CA3EC;
                border: none;
                color: white;
                font-weight: bold;
            }

            button[kind="primary"]:hover {
                background-color: #1485C6;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.title("Registro de Pacientes")

        with st.form("form_registro"):
            nombre = st.text_input("Nombre")
            apellido = st.text_input("Apellido (puede ser dos palabras)")
            email = st.text_input("Correo electrónico")
            presupuesto = st.text_input("Presupuesto")
            guardar = st.form_submit_button("Guardar", type="primary")

        if guardar:
            if nombre == "" or apellido == "" or email == "" or presupuesto == "":
                st.warning("Todos los campos son obligatorios")
            else:
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
                    st.error("Datos inválidos. Verifique la información ingresada")

        st.subheader("Tabla de Pacientes")
        datos = self.lpersona.mostrarPersona()
        st.dataframe(datos, use_container_width=True)
