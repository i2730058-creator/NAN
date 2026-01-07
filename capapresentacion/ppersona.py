import streamlit as st
from capalogica.lpersona import LPersona

class PPersona:
    def __init__(self):
        self.lpersona = LPersona()
        self.construirInterfaz()

    def construirInterfaz(self):
        st.set_page_config(page_title="MOOVA CLINIC", layout="wide")
        st.title("MOOVA CLINIC")
        st.markdown("### Registro de Pacientes")

        with st.form("formulario_registro"):
            col1, col2 = st.columns(2)
            with col1:
                txtnombre = st.text_input("Nombre")
                txtapellido = st.text_input("Apellido (dos apellidos juntos separados por espacio)")
            with col2:
                txtemail = st.text_input("Correo electrónico")
                txtsalario = st.number_input("Salario", min_value=1000.0)
            btnGuardar = st.form_submit_button("Guardar", type="primary")

        if btnGuardar:
            persona = {
                "nombre": txtnombre.strip(),
                "apellido": txtapellido.strip(),  # columna correcta
                "email": txtemail.strip(),
                "salario": int(txtsalario)
            }
            resultado = self.lpersona.insertarPersona(persona)
            if resultado:
                st.success("Registro guardado correctamente")
            else:
                st.error("No se pudo guardar el registro. Verifica los datos.")

        st.markdown("---")
        st.markdown("### Tabla de Pacientes")
        listaPersonas = self.lpersona.mostrarPersonas()
        if listaPersonas:
            st.dataframe(listaPersonas, use_container_width=True)
        else:
            st.info("No hay registros para mostrar.")

        st.markdown("---")
        st.markdown("### Eliminar Paciente")
        id_eliminar = st.number_input("ID a eliminar", min_value=1, step=1)
        if st.button("Eliminar"):
            if self.lpersona.eliminarPersona(int(id_eliminar)):
                st.success(f"Registro con ID {id_eliminar} eliminado")
            else:
                st.error("No se pudo eliminar el registro")
