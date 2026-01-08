import streamlit as st
from capalogica.lpersona import LPersona

class PPersona:
    def __init__(self):
        self.lpersona = LPersona()
        self.construir()

    def construir(self):

        st.set_page_config(layout="wide")

        st.markdown("""
        <style>
        .stApp {
            background-color: #0E1117;
            color: #E6E6E6;
        }

        h1, h2 {
            color: #4FC3F7;
        }

        label, span, p {
            color: #E6E6E6 !important;
        }

        input {
            background-color: #1C1F26 !important;
            color: #E6E6E6 !important;
        }

        div[data-baseweb="input"] > div {
            background-color: #1C1F26;
        }

        button {
            background-color: #4FC3F7 !important;
            color: black !important;
            font-weight: bold;
            border: none !important;
        }

        button:hover {
            background-color: #29B6F6 !important;
        }
        </style>
        """, unsafe_allow_html=True)

        st.title("Gestión de Pacientes")

        with st.form("form_paciente"):

            top_left, top_right = st.columns([5, 1])

            with top_right:
                actualizar = st.form_submit_button("✏️")
                eliminar = st.form_submit_button("🗑️")

            col1, col2 = st.columns(2)

            with col1:
                id_paciente = st.number_input("ID (editar o eliminar)", min_value=0, step=1)
                nombre = st.text_input("Nombre")
                apellido = st.text_input("Apellido")

            with col2:
                email = st.text_input("Correo electrónico")
                presupuesto = st.text_input("Presupuesto")

            guardar = st.form_submit_button("Guardar", type="primary")

        # ---------- ACCIONES ----------
        if guardar:
            if not nombre or not apellido or not email or not presupuesto:
                st.warning("Completa todos los campos")
            else:
                persona = {
                    "nombre": nombre.strip(),
                    "apellido": apellido.strip(),
                    "email": email.strip(),
                    "presupuesto": presupuesto.strip()
                }
                if self.lpersona.nuevaPersona(persona):
                    st.success("Paciente registrado")
                    st.rerun()
                else:
                    st.error("Datos inválidos")

        if actualizar:
            if id_paciente == 0:
                st.warning("Ingresa el ID para actualizar")
            else:
                persona = {
                    "id": int(id_paciente),
                    "nombre": nombre.strip(),
                    "apellido": apellido.strip(),
                    "email": email.strip(),
                    "presupuesto": presupuesto.strip()
                }
                self.lpersona.actualizarPersona(persona)
                st.success("Paciente actualizado")
                st.rerun()

        if eliminar:
            if id_paciente == 0:
                st.warning("Ingresa el ID para eliminar")
            else:
                self.lpersona.eliminarPersona(int(id_paciente))
                st.success("Paciente eliminado")
                st.rerun()

        st.subheader("Listado de pacientes")
        datos = self.lpersona.mostrarPersona()
        st.dataframe(datos, use_container_width=True)
