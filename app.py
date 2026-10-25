import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado principal de la aplicación
st.header('Cuadro de Mandos: Análisis de Vehículos Usados')

# Lectura de los datos
car_data = pd.read_csv('vehicles_us.csv')

# Visualización rápida de los datos
st.write('Exploración visual del inventario de anuncios de venta de coches:')

# --- Sección 1: Histograma ---
st.subheader('Distribución del Odómetro')
build_histogram = st.checkbox('Construir un histograma del odómetro')

if build_histogram:
    st.write('Generando histograma de kilometraje (odómetro)...')
    fig_hist = px.histogram(
        car_data, 
        x='odometer', 
        title='Distribución de Kilometraje (Odómetro)',
        labels={'odometer': 'Kilometraje'}
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# --- Sección 2: Diagrama de Dispersión ---
st.subheader('Relación entre Kilometraje y Precio')
build_scatter = st.checkbox('Construir un gráfico de dispersión (Odómetro vs. Precio)')

if build_scatter:
    st.write('Generando gráfico de dispersión de precio en función del odómetro...')
    fig_scatter = px.scatter(
        car_data, 
        x='odometer', 
        y='price', 
        title='Precio vs. Kilometraje',
        labels={'odometer': 'Kilometraje', 'price': 'Precio (USD)'},
        opacity=0.5
    )
    st.plotly_chart(fig_scatter, use_container_width=True)