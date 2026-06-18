import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("vehicles_us.csv")

st.header("Dashboard de Anúncios de Veículos")
st.write("Análise exploratória de anúncios de veículos usados.")

build_histogram = st.checkbox("Criar histograma da quilometragem")

if build_histogram:
    st.write("Criando um histograma para a coluna odometer")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox("Criar gráfico de dispersão preço vs quilometragem")

if build_scatter:
    st.write("Criando um gráfico de dispersão para price e odometer")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
