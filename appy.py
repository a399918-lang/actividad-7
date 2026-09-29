import streamlit as st

st.title("Evaluación de un lote")
st.sidebar.write("Diana Valeria Soto Mendez 3L Facultad de Ciencias Quimicas")

pH = st.number_input(
    "pH",
    value=6.5
)

temperatura = st.number_input(
    "Temperatura (°C)",
    value=23.0
)

if st.button("Evaluar"):
    if pH < 6.8 or pH > 7.9:
        resultado = "Revisar pH"
    elif temperatura < 20 or temperatura > 25:
        resultado = "Revisar temperatura"
    else:
        resultado = "Lote aceptable"

    st.write(f"Resultado: {resultado}")
