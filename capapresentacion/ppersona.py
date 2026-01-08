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
            border: none !important;
        }

        button:hover {
            background-color: #29B6F6 !important;
        }
        </style>
        """, unsafe_allow_html=True)

        st.title("Gestión de Pacientes")

        with st.form("form_paciente"):

            header_left, header_right = st.columns([6, 1])

            with header_right:
                editar = st.form_submit_button("✏️", use_container_width=True)

            col1, col2 = st.columns(2)

            with col1:
                id_paciente = st.number_input("ID", min_value=0, step=1)
                nombre = st.text_input("Nombre")
                apellido = st.text_input("Apellido")

            with col2:
                email = st.text_input("Correo electrónico")
                presupuesto = st.text_input("Presupuesto")

            acciones_izq, acciones_der = st.columns(2)

            with acciones_izq:
                eliminar = st.form_submit_button("🗑️ Eliminar")

            with acciones_der:
                guardar = st.form_submit_button("Guardar", type="primary")

        # ---------- VALIDACIÓN ----------
        campos_completos = (
            nombre.strip() != "" and
            apellido.strip() != "" and
            email.strip() != "" and
            presupuesto.strip() != ""
        )

        if guardar:
            if not campos_completos:
                st.warning("Debes completar todos los campos")
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

        if editar:
            if id_paciente == 0 or not campos_completos:
                st.warning("Completa todos los campos e ingresa el ID")
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
                st.warning("Ingresa el ID a eliminar")
            else:
                self.lpersona.eliminarPersona(int(id_paciente))
                st.success("Paciente eliminado")
                st.rerun()

        st.subheader("Listado de pacientes")
        st.dataframe(self.lpersona.mostrarPersona(), use_container_width=True)
