import streamlit as st
from capalogica.lpersona import LPersona

class PPersona:
    def __init__(self):
        self.lpersona = LPersona()
        self.construir()

    def construir(self):

        st.markdown("""
        <style>
        .stApp {
            background-color: #0E1117;
            color: #E6E6E6;
        }

        h1, h2, h3 {
            color: #4FC3F7;
        }

        label, p, span {
            color: #E6E6E6 !important;
        }

        input, textarea {
            background-color: #1C1F26 !important;
            color: #E6E6E6 !important;
        }

        div[data-baseweb="input"] > div {
            background-color: #1C1F26;
        }

        button[kind="primary"] {
            background-color: #4FC3F7;
            color: black;
            font-weight: bold;
            border: none;
        }

        button[kind="primary"]:hover {
            background-color: #29B6F6;
            color: black;
        }

        </style>
        """, unsafe_allow_html=True)

        st.title("Registro de Pacientes")

        with st.form("form_registro"):
            nombre = st.text_input("Nombre")
            apellido = st.text_input("Apellido")
            email = st.text_input("Correo electrónico")
            presupuesto = st.text_input("Presupuesto")
            guardar = st.form_submit_button("Guardar", type="primary")

        if guardar:
            if not nombre or not apellido or not email or not presupuesto:
                st.warning("Todos los campos son obligatorios")
            else:
                persona = {
                    "nombre": nombre.strip(),
                    "apellido": apellido.strip(),
                    "email": email.strip(),
                    "presupuesto": presupuesto.strip()
                }

                if self.lpersona.nuevaPersona(persona):
                    st.success("Paciente registrado correctamente")
                    st.rerun()
                else:
                    st.error("Los datos ingresados no son válidos")

        st.subheader("Lista de Pacientes")
        datos = self.lpersona.mostrarPersona()
        st.dataframe(datos, use_container_width=True)
