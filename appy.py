import streamlit as st
st. titlet"Evaluación de un lote")
ph - st. number_input(
"pH"
value=6.5
temperatura = st.number_input(
"Temperatura (°C)", value=23.0
if st. button( Evaluar"):
it pH < 6.8 or рн > 7.9:
resultado - "Revisar pH"
eLit
temperatura ‹ 20 or temperatura > 25:
resultado = "Revisar temperatura"
else:
resultado = "Lote aceptable"
st.write (f"Resultado: (resultado))
