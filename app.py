import streamlit as st
from textblob import TextBlob

# Título de la aplicación
st.title('Detector de Emociones')

# Funciones para cambiar el fondo y agregar animaciones según la emoción
def cambiar_fondo_azul():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #ADD8E6;
        }
        </style>
        """, unsafe_allow_html=True)

def cambiar_fondo_rosado():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #FFB6C1;
        }
        </style>
        """, unsafe_allow_html=True)

def cambiar_fondo_rojo():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #FF6347;
        }
        </style>
        """, unsafe_allow_html=True)

# Animación para la rabia: barra de progreso
def animacion_rabia():
    st.write("😡 Tu rabia está aumentando...")
    progress_bar = st.progress(0)
    for i in range(100):
        progress_bar.progress(i + 1)

# Pregunta al usuario cómo se siente
st.subheader("¿Cómo te sientes hoy? (Escribe: feliz, triste o enojado)")
emocion = st.text_input("Escribe tu emoción:").strip().lower()

# Mostrar respuesta creativa según la emoción
if emocion == 'triste':
    cambiar_fondo_azul()
    st.snow()  # Animación de nieve para tristeza
    st.write("😢 Lo siento, parece que estás triste. ¡Espero que pronto te sientas mejor!")
elif emocion == 'feliz':
    cambiar_fondo_rosado()
    st.balloons()  # Animación de globos para felicidad
    st.write("😊 ¡Qué bien! Estás feliz, sigue con esa actitud positiva.")
elif emocion == 'enojado':
    cambiar_fondo_rojo()
    animacion_rabia()  # Animación de barra de progreso para la rabia
    st.write("😡 Parece que estás enojado. ¡Respira hondo, todo estará bien pronto!")
elif emocion:  # Si escribe algo diferente
    st.write("Por favor, escribe solo: feliz, triste o enojado.")

# Expander para el análisis de texto
with st.expander('Analizar Polaridad y Subjetividad en un texto'):
    text1 = st.text_area('Escribe por favor: ')
    if text1:
        blob = TextBlob(text1)
        
        st.write('Polarity: ', round(blob.sentiment.polarity, 2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity, 2))

# Expander para corrección de texto en inglés
with st.expander('Corrección en inglés'):
    text2 = st.text_area('Escribe por favor: ', key='4')
    if text2:
        blob2 = TextBlob(text2)
        st.write(blob2.correct())
