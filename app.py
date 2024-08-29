import streamlit as st
from textblob import TextBlob
import language_tool_python

st.title('Uso de TextBlob y LanguageTool')

st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")
with st.sidebar:
    st.subheader("Polaridad y Subjetividad")
    st.markdown("""
    **Polaridad**: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
    Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.
    
    **Subjetividad**: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
    (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.
    """)

with st.expander('Analizar Polaridad y Subjetividad en un texto'):
    text1 = st.text_area('Escribe por favor en español: ')
    if text1:
        blob = TextBlob(text1)
        st.write('Polaridad: ', round(blob.sentiment.polarity, 2))
        st.write('Subjetividad: ', round(blob.sentiment.subjectivity, 2))
        x = round(blob.sentiment.polarity, 2)
        if x >= 0.5:
            st.write('Es un sentimiento Positivo 😊')
        elif x <= -0.5:
            st.write('Es un sentimiento Negativo 😔')
        else:
            st.write('Es un sentimiento Neutral 😐')

with st.expander('Corrección en español'):
    text2 = st.text_area('Escribe por favor en español:', key='4')
    if text2:
        tool = language_tool_python.LanguageTool('es')
        matches = tool.check(text2)
        corrected_text = language_tool_python.utils.correct(text2, matches)
        st.write(corrected_text)
