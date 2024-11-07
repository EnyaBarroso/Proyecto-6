import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

# Encabezado de la aplicación
st.header('Conjunto de Datos de Anuncios de Coches')

# Botón para generar el histograma
hist_button = st.button('Construir histograma') # boton de histograma
if hist_button:
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # Generar histograma con Plotly Express
    fig = px.histogram(car_data, x='odometer')  # Columna que deseo graficar
    st.plotly_chart(fig, use_container_width=True)  # Muestra el gráfico en la aplicación

# Botón para generar el gráfico de dispersión
if hist_button('Generar Gráfico de Dispersión'):
    scatter_button = st.button('Generar Gráfico de Dispersión')  # Botón de dispersión
    # escribir un mensaje
    st.write('Creación de un Gráfico de Dispersión para el conjunto de datos de anuncios de venta de coches')
    # Generar gráfico de dispersión con Plotly Express
    fig = px.scatter(car_data, x='odometer', y='price')  #columnas deseadas
    st.plotly_chart(fig, use_container_width=True)  # Muestra el gráfico en la aplicación
    