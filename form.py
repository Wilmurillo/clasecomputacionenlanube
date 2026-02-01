import streamlit as st

st.title("Formulario de Registro Estudiantil IP-2026")

nombre = st.text_input("Nombre completo")
edad=st.number_input("Edad", min_value=0, max_value=80)
carrera=st.selectbox("Carrera", ["Ingeniería en Computación","Diseño Web","Diplomado en Computación"])
comentario=st.text_area("Comentario adicional (opcional)")


if st.button("Enviar"):
    st.write("### Datos ingresados:")
    st.write(f"**Nombre:** {nombre}")
    st.write(f"**Edad:** {edad}")
    st.write(f"**Carrera:** {carrera}")
    st.write(f"**Comentario:** {comentario}")
    st.success(" Formulario enviado con éxito.")