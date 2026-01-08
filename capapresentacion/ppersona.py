import streamlit as st
from capalogica.lpersona import LPersona

class PPersona:
    def __init__(self):
        self.lpersona = LPersona()
        if "modo_edicion" not in st.session_state:
            st.session_state.modo_edicion = False
        if "persona_editando" not in st.session_state:
            st.session_state.persona_editando = {}

        self.construir()

    def construir(self):

        st.set_page_config(layout="wide")
        st.title("Registro de Pacientes")

        col1, col2 = st.columns(2)

        with col1:
            id_paciente = st.number_input("ID del paciente", min_value=0, step=1)

        with col2:
            editar = st.button("Editar")

        if editar:
            datos = self.lpersona.mostrarPersonas()
            for p in datos:
                if p["id"] == id_paciente:
                    st.session_state.persona_editando = p
                    st.session_state.modo_edicion = True
                    break

        nombre = st.text_input(
            "Nombre",
            value=st.session_state.persona_editando.get("nombre", "")
        )
        apellido = st.text_input(
            "Apellido",
            value=st.session_state.persona_editando.get("apellido", "")
        )
        email = st.text_input(
            "Correo electrónico",
            value=st.session_state.persona_editando.get("email", "")
        )
        presupuesto = st.text_input(
            "Presupuesto",
            value=str(st.session_state.persona_editando.get("presupuesto", ""))
        )

        if st.session_state.modo_edicion:
            guardar = st.button("Guardar cambios")

            if guardar:
                if (
                    nombre.strip() == "" or
                    apellido.strip() == "" or
                    email.strip() == "" or
                    presupuesto.strip() == ""
                ):
                    st.warning("Completa todos los campos")
                else:
                    persona = {
                        "id": id_paciente,
                        "nombre": nombre.strip(),
                        "apellido": apellido.strip(),
                        "email": email.strip(),
                        "presupuesto": presupuesto.strip()
                    }
                    self.lpersona.actualizarPersona(persona)
                    st.success("Paciente actualizado")
                    st.session_state.modo_edicion = False
                    st.session_state.persona_editando = {}
                    st.rerun()

        st.divider()

        st.subheader("Eliminar paciente")
        id_eliminar = st.number_input("ID a eliminar", min_value=0, step=1, key="del")
        if st.button("Eliminar"):
            if id_eliminar > 0:
                self.lpersona.eliminarPersona(id_eliminar)
                st.success("Paciente eliminado")
                st.rerun()

        st.subheader("Listado de pacientes")
        st.dataframe(self.lpersona.mostrarPersonas(), use_container_width=True)
