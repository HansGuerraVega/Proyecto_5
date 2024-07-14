import pandas as pd
import streamlit as st
import plotly.express as px

print('En esta pagina encontrarás dos botones, uno grafica un histograma de') 
print('la cantidad de coches con ciertos kilómetris y el otro una gráfica de') 
print('dispersión de cómo cambia el precio dependiendo del kilometraje')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
dispersion_button = st.button('Construir una gráfica de dispersión') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if dispersion_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un una gráfica de dipersión para el conjunto de datos de anuncios de venta de coches')
    
    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price") 

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    