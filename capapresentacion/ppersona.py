import streamlit as st
from capalogica.lpersona import LPersona

class PPersona:
    def __init__(self):
        self.lpersona = LPersona()
        self.construir()

    def construir(self):
        st.title("Registro de Pacientes")

        if "editando" not in st.session_state:
            st.session_state.editando = False
        if "persona_edit" not in st.session_state:
            st.session_state.persona_edit = {}

        col1, col2 = st.columns([2, 1])

        with col1:
            nombre = st.text_input(
                "Nombre",
                value=st.session_state.persona_edit.get("nombre", "")
            )
            apellido = st.text_input(
                "Apellido",
                value=st.session_state.persona_edit.get("apellido", "")
            )
            email = st.text_input(
                "Correo electrónico",
                value=st.session_state.persona_edit.get("email", "")
            )
            presupuesto = st.text_input(
                "Presupuesto",
                value=st.session_state.persona_edit.get("presupuesto", "")
            )

            if st.session_state.editando:
                if st.button("Actualizar"):
                    persona = {
                        "id": st.session_state.persona_edit["id"],
                        "nombre": nombre,
                        "apellido": apellido,
                        "email": email,
                        "presupuesto": presupuesto
                    }

                    if self.lpersona.actualizarPersona(persona):
                        st.session_state.editando = False
                        st.session_state.persona_edit = {}
                        st.rerun()
            else:
                if st.button("Guardar"):
                    persona = {
                        "nombre": nombre,
                        "apellido": apellido,
                        "email": email,
                        "presupuesto": presupuesto
                    }

                    if self.lpersona.nuevaPersona(persona):
                        st.rerun()

        st.divider()

        st.subheader("Buscar paciente")
        texto_buscar = st.text_input("Buscar por nombre o apellido")

        datos = self.lpersona.mostrarPersonas()

        if texto_buscar != "":
            datos = [
                p for p in datos
                if texto_buscar.lower() in p["nombre"].lower()
                or texto_buscar.lower() in p["apellido"].lower()
            ]

        st.subheader("Listado de Pacientes")
        st.dataframe(datos, use_container_width=True)

        st.divider()

        st.subheader("Editar paciente")
        id_editar = st.number_input("ID a editar", min_value=0, step=1)

        if st.button("Cargar datos"):
            for p in self.lpersona.mostrarPersonas():
                if p["id"] == id_editar:
                    st.session_state.persona_edit = p
                    st.session_state.editando = True
                    st.rerun()

        st.divider()

        st.subheader("Eliminar paciente")
        id_eliminar = st.number_input("ID a eliminar", min_value=0, step=1, key="del")

        if st.button("Eliminar"):
            self.lpersona.eliminarPersona(id_eliminar)
            st.rerun()
