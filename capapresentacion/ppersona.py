import streamlit as st
from capalogica.lpersona import LPersona

class PPersona:
    def __init__(self):
        self.lpersona = LPersona()
        self.construir()

    def construir(self):
        st.set_page_config(layout="wide")
        st.title("MOOVA CLINIC – Registro de Pacientes")

        col_form, col_delete = st.columns([3, 1])

        with col_form:
            st.subheader("Datos del paciente")

            nombre = st.text_input("Nombre")
            apellido = st.text_input("Apellido")
            email = st.text_input("Correo electrónico")
            presupuesto = st.number_input("Presupuesto", min_value=0.0)

            if st.button("Guardar"):
                if not nombre or not apellido or not email:
                    st.warning("Complete todos los campos")
                else:
                    persona = {
                        "nombre": nombre.strip(),
                        "apellido": apellido.strip(),
                        "email": email.strip(),
                        "presupuesto": presupuesto
                    }

                    if self.lpersona.insertarPersona(persona):
                        st.success("Paciente registrado")
                        st.rerun()
                    else:
                        st.error("No se pudo guardar")

        with col_delete:
            st.subheader("Eliminar paciente")
            id_eliminar = st.number_input("ID a eliminar", min_value=1, step=1)

            if st.button("Eliminar"):
                if self.lpersona.eliminarPersona(id_eliminar):
                    st.success("Paciente eliminado")
                    st.rerun()
                else:
                    st.error("Error al eliminar")

        st.divider()
        st.subheader("Listado de pacientes")

        datos = self.lpersona.mostrarPersonas()
        st.dataframe(datos, use_container_width=True)
