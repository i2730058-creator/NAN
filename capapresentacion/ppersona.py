from capalogica.lpersona import LPersona
import streamlit as st

class PPersona:
    def __init__(self):
        self.lpersona = LPersona()
        self.construirInterfaz()

    def construirInterfaz(self):
        st.title('MOOVA CLINIC')
        with st.form('formulario Registro'):
            txtdoidentidad = st.text_input('Documento de identidad')
            txtnombre = st.text_input('Nombre')
            txtedad = st.number_input('Edad', min_value=0)
            btnGuardar = st.form_submit_button('Guardar', type='primary')

        if btnGuardar:
            persona = {
                'docidentidad': txtdoidentidad,
                'nombre': txtnombre,
                'edad': txtedad
            }
            self.insertarpersona(persona)
            self.mostrarPersonas()

    def mostrarPersonas(self):
        listaPersonas = self.lpersona.mostrarPersonas()
        
        if isinstance(listaPersonas, list):
            if len(listaPersonas) > 0:
                st.dataframe(listaPersonas, selection_mode='single-row', on_select='rerun')
            else:
                st.warning("No hay personas registradas.")
        else:
            st.error(f"Error al obtener los datos: {listaPersonas}")

    def insertarpersona(self, persona: dict):
        self.lpersona.insertarpersona(persona)
        st.toast('Registro guardado correctamente', icon='👌', duration=2)
