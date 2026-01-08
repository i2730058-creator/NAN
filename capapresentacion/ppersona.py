with col1:
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
        id_editar = st.number_input(
            "ID a editar",
            min_value=0,
            step=1
        )

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
