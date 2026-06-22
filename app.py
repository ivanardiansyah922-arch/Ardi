import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard Weather",
    page_icon="🌤️",
    layout="wide"
)

@st.cache_data
def load_data(file):
    return pd.read_csv(file)

st.title("🌤️ Dashboard Analisis Cuaca")

uploaded_file = st.file_uploader(
    "Upload weather.csv",
    type=["csv"]
)

if uploaded_file:

    df = load_data(uploaded_file)

    st.success(f"Data berhasil dimuat ({len(df)} data)")

    st.subheader("Preview Data")
    st.dataframe(df)

    # KPI
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Rata-rata Suhu",
            f"{df['Suhu'].mean():.2f} °C"
        )

    with col2:
        st.metric(
            "Rata-rata Kelembaban",
            f"{df['Kelembaban'].mean():.2f}%"
        )

    with col3:
        st.metric(
            "Rata-rata Angin",
            f"{df['Angin'].mean():.2f} km/jam"
        )

    st.divider()

    st.subheader("Distribusi Cuaca")

    fig1 = px.pie(
        df,
        names="Cuaca",
        hole=0.4
    )

    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("Suhu Berdasarkan Cuaca")

    fig2 = px.box(
        df,
        x="Cuaca",
        y="Suhu",
        color="Cuaca"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Kelembaban vs Suhu")

    fig3 = px.scatter(
        df,
        x="Suhu",
        y="Kelembaban",
        color="Cuaca",
        size="Angin"
    )

    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("Statistik Data")

    st.dataframe(df.describe())

else:
    st.info("Upload file weather.csv terlebih dahulu.")