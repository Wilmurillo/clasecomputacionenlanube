import streamlit as st

st.title("Este es un conversor de Lempiras a Dolares")

lempiras=st.number_input('Ingrese la cantidad de Lempiras', min_value=0.0)

if st.button ('Procesar'):
    dolares=lempiras/26.50
    st.write(f"El equivalente en dolares es : ${dolares:.2f}") 