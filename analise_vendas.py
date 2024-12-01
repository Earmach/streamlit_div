import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

with st.sidebar:
    st.title("Análise de lucro")
    uploaded_file = st.file_uploader("Coloque o seu arquivo aqui (CSV)", type=["csv"])

# para fazer a leitura dos dados
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    with st.sidebar:
        distinct_regions = df["Region"].unique().tolist()
        region_selected = st.selectbox("região específica", distinct_regions)

        seller_selected: object = st.radio("Vendedor", ["H", "C", "M", "L"], index=None)


        if region_selected:
            df = df[df["Region"] == region_selected]

        if seller_selected:
            df = df[df["Order Priority"] == seller_selected]

    # Escrevendo em um campo dentro do IF inicial (se o arquivo não for vazio)
    st.write("Lucro por tipo de item")
    st.bar_chart(df, x="Item Type", y="Total Profit")
    st.dataframe(df, use_container_width=True)