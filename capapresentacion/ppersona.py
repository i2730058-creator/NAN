import streamlit as st
from capalogica.lpersona import LPersona

class PPersona:
    def __init__(self):
        self.logica = LPersona()
        self.ui()

    def ui(self):
        st.set_page_config(layout="wide")
        st.title("Clínica – Gestión de Pacientes")

        st.subheader("Registro / Edición de Pacientes")

        col1, col2 = st.columns([2, 1])

        with col1:
            id_editar = st.number_input("ID (solo para editar)", min_value=0, step=1)
            nombre = st.text_input("Nombre")
            apellido = st.text_input("Apellido (puede ser dos palabras)")
            email = st.text_input("Correo electrónico")
            presupuesto = st.number_input("Presupuesto", min_value=0.0)

            col_btn1, col_btn2 = st.columns(2)

            with col_btn1:
                if st.button("Guardar"):
                    if nombre and apellido and email and presupuesto > 0:
                        persona = {
                            "nombre": nombre,
                            "apellido": apellido,
                            "email": email,
                            "presupuesto": presupuesto
                        }
                        self.logica.nuevaPersona(persona)
                        st.success("Paciente registrado")
                        st.rerun()
                    else:
                        st.warning("Complete todos los campos")

            with col_btn2:
                if st.button("Actualizar"):
                    if id_editar > 0 and nombre and apellido and email and presupuesto > 0:
                        persona = {
                            "nombre": nombre,
                            "apellido": apellido,
                            "email": email,
                            "presupuesto": presupuesto
                        }
                        self.logica.actualizarPersona(persona, id_editar)
                        st.success("Paciente actualizado")
                        st.rerun()
                    else:
                        st.warning("Ingrese ID y todos los datos")

        with col2:
            st.subheader("Eliminar paciente")
            id_eliminar = st.number_input("ID a eliminar", min_value=0, step=1)

            if st.button("Eliminar"):
                if id_eliminar > 0:
                    self.logica.eliminarPersona(id_eliminar)
                    st.success("Paciente eliminado")
                    st.rerun()
                else:
                    st.warning("Ingrese un ID válido")

        st.divider()

        st.subheader("Listado de Pacientes")

        datos = self.logica.mostrarPersona()

        buscar = st.text_input("Buscar por nombre, apellido o correo")

        if buscar:
            datos = [
                d for d in datos
                if buscar.lower() in d["nombre"].lower()
                or buscar.lower() in d["apellido"].lower()
                or buscar.lower() in d["email"].lower()
            ]

        st.dataframe(datos, use_container_width=True)
