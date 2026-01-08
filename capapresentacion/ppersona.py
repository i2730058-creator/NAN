def construir(self):
    st.title("Registro de Pacientes")

    col1, col2 = st.columns([2, 1])  # ← AQUÍ se crean

    with col1:
        nombre = st.text_input("Nombre")
        apellido = st.text_input("Apellido")
        email = st.text_input("Correo electrónico")
        presupuesto = st.number_input("Presupuesto", min_value=0.0)

        if st.button("Guardar"):
            pass

    with col2:
        st.subheader("Eliminar paciente")
