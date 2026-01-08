import streamlit as st
from capalogica.lpersona import LPersona

class PPersona:
    def __init__(self):
        self.lpersona = LPersona()
        self.construir()

    def construir(self):

        st.set_page_config(layout="wide")

        st.title("Registro de Pacientes")

        with st.form("form_registro"):

            col1, col2 = st.columns(2)

            with col1:
                id_paciente = st.number_input("ID (para editar)", min_value=0, step=1)
                nombre = st.text_input("Nombre")
                apellido = st.text_input("Apellido")

            with col2:
                email = st.text_input("Correo electrónico")
                presupuesto = st.text_input("Presupuesto")

            btn_guardar, btn_editar = st.columns([4, 1])

            with btn_guardar:
                guardar = st.form_submit_button("Guardar")

            with btn_editar:
                st.markdown("<small>&nbsp;</small>", unsafe_allow_html=True)
                editar = st.form_submit_button("Editar")

        # Validación básica
        campos_completos = (
            nombre.strip() != "" and
            apellido.strip() != "" and
            email.strip() != "" and
            presupuesto.strip() != ""
        )

        if guardar:
            if not campos_completos:
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
                    st.error("No se pudo guardar")

        if editar:
            if id_paciente == 0 or not campos_completos:
                st.warning("Ingresa el ID y completa todos los campos")
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

        st.divider()

        st.subheader("Eliminar paciente")

        col_del_1, col_del_2 = st.columns([3, 1])

        with col_del_1:
            id_eliminar = st.number_input("ID a eliminar", min_value=0, step=1, key="del")

        with col_del_2:
            eliminar = st.button("Eliminar")

        if eliminar:
            if id_eliminar == 0:
                st.warning("Ingresa un ID válido")
            else:
                self.lpersona.eliminarPersona(int(id_eliminar))
                st.success("Paciente eliminado")
                st.rerun()

        st.subheader("Listado de pacientes")
        st.dataframe(self.lpersona.mostrarPersona(), use_container_width=True)
