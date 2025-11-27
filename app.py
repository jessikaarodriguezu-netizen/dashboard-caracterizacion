
import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def cargar_datos():
    url = "https://docs.google.com/spreadsheets/d/1E9VCBy5C_OJrsVeZxqKRsC8EYyki3k3yK7XwDy9VcV/export?format=csv"
    df = pd.read_csv(url)

    df = df.rename(columns={
        'sec': 'id',
        '11. Franja horaria en la que estudia': 'franja',
        '27. Su vivienda actual es:': 'tipo_vivienda',
        '37. Estrato socioeconómico de la vivienda:': 'estrato',
        '42. ¿Trabaja este periodo mientras estudia?': 'trabaja',
        '55. ¿Frecuencia que utiliza los siguientes medios de comunicación? [Internet]': 'internet'
    })
    return df

df = cargar_datos()

st.set_page_config(page_title="Dashboard de Caracterización", layout="wide")
st.title("📊 Dashboard de Caracterización Estudiantil")
st.write("Interactúa con los filtros para explorar los datos de la encuesta.")

st.sidebar.header("Filtros")

franja_sel = st.sidebar.multiselect(
    "Selecciona la franja horaria:",
    df["franja"].unique(),
    default=df["franja"].unique()
)

df_filtrado = df[df["franja"].isin(franja_sel)]

st.subheader("1. Distribución de Estrato Socioeconómico")
fig1 = px.histogram(df_filtrado, x="estrato", color="estrato", text_auto=True,
                    title="Estrato Socioeconómico")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("2. Trabajo según Franja Horaria")
fig2 = px.histogram(df_filtrado, x="franja", color="trabaja",
                    barmode="group", text_auto=True,
                    title="Trabajo vs Franja")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("3. Tipo de Vivienda")
fig3 = px.histogram(df_filtrado, x="tipo_vivienda", color="tipo_vivienda",
                    text_auto=True, title="Tipo de Vivienda")
st.plotly_chart(fig3, use_container_width=True)

st.subheader("4. Frecuencia de Uso de Internet")
fig4 = px.histogram(df_filtrado, x="internet", color="internet",
                    text_auto=True, title="Frecuencia de Internet")
st.plotly_chart(fig4, use_container_width=True)

st.write("---")
st.write("Desarrollado por Jessika Rodríguez Ussa y Luis Antonio Bernal Suárez")
