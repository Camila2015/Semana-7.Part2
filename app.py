import streamlit as st
from textblob import TextBlob
from googletrans import Translator

translator = Translator()
st.title('Uso de TextBlob')

st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")
with st.sidebar:
    st.subheader("Polaridad y Subjetividad")
    st.write("""
        **Polaridad**: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral.
        Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.

        **Subjetividad**: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
        (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.
    """)

# Función creativa para cambiar el estilo según la polaridad
def cambiar_fondo_positivo():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #DFF7DF;
        }
        </style>
        """, unsafe_allow_html=True)

def cambiar_fondo_negativo():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #F8D7DA;
        }
        </style>
        """, unsafe_allow_html=True)

def cambiar_fondo_neutral():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #F3F4F6;
        }
        </style>
        """, unsafe_allow_html=True)

def mensaje_creativo_positivo():
    st.balloons()
    st.write("🎉 ¡El mundo es un lugar maravilloso, sigue con esa energía positiva!")

def mensaje_creativo_negativo():
    st.write("🌧️ A veces las nubes oscuras nos envuelven, pero siempre hay un rayo de sol esperando.")

def mensaje_creativo_neutral():
    st.write("🌀 La calma puede ser un gran lugar para reflexionar y encontrar balance.")

with st.expander('Analizar Polaridad y Subjetividad en un texto'):
    text1 = st.text_area('Escribe por favor: ')
    if text1:
        blob = TextBlob(text1)
        
        st.write('Polarity: ', round(blob.sentiment.polarity, 2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity, 2))
        x = round(blob.sentiment.polarity, 2)

        # Creatividad según el sentimiento
        if x >= 0.5:
            cambiar_fondo_positivo()
            mensaje_creativo_positivo()
        elif x <= -0.5:
            cambiar_fondo_negativo()
            mensaje_creativo_negativo()
        else:
            cambiar_fondo_neutral()
            mensaje_creativo_neutral()

with st.expander('Corrección en inglés'):
    text2 = st.text_area('Escribe por favor: ', key='4')
    if text2:
        blob2 = TextBlob(text2)
        st.write(blob2.correct())
