import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Football Data Insights",
    layout="wide"
)

st.markdown("""
<style>
    .stApp {
        background-color: #121826;
        color: #F5F5F5;
    }

    [data-testid="stMetric"] {
        background-color: #1B4332;
        padding: 18px;
        border-radius: 10px;
    }

    h1, h2, h3 {
        color: #2ECC71;
    }
</style>
""", unsafe_allow_html=True)


@st.cache_data
def carregar_dados():
    return pd.read_csv("player_stats.csv")


jogadores = carregar_dados()

st.title("Football Data Insights")
st.write(
    "Análise exploratória de dados de jogadores do FIFA 24."
)

st.divider()

st.subheader("Filtros")

col1, col2 = st.columns(2)

with col1:
    paises = sorted(jogadores["country"].dropna().unique())

    pais_selecionado = st.selectbox(
        "País",
        ["Todos"] + paises
    )

with col2:
    idade_min = int(jogadores["age"].min())
    idade_max = int(jogadores["age"].max())

    faixa_idade = st.slider(
        "Faixa de idade",
        min_value=idade_min,
        max_value=idade_max,
        value=(idade_min, idade_max)
    )

dados_filtrados = jogadores.copy()

if pais_selecionado != "Todos":
    dados_filtrados = dados_filtrados[
        dados_filtrados["country"] == pais_selecionado
    ]

dados_filtrados = dados_filtrados[
    dados_filtrados["age"].between(
        faixa_idade[0],
        faixa_idade[1]
    )
]

st.write(
    f"Jogadores encontrados: **{len(dados_filtrados)}**"
)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total de jogadores",
        f"{len(dados_filtrados):,}".replace(",", ".")
    )

with col2:
    idade_media = dados_filtrados["age"].mean()
    st.metric(
        "Idade média",
        f"{idade_media:.1f} anos"
        if not dados_filtrados.empty else "N/A"
    )

with col3:
    controle_medio = dados_filtrados["ball_control"].mean()
    st.metric(
        "Média de controle de bola",
        f"{controle_medio:.1f}"
        if not dados_filtrados.empty else "N/A"
    )

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Jogadores por idade")

    jogadores_por_idade = (
        dados_filtrados["age"]
        .value_counts()
        .sort_index()
    )

    st.bar_chart(jogadores_por_idade)

with col2:
    st.subheader("Clubes com mais jogadores")

    top_clubes = (
        dados_filtrados["club"]
        .value_counts()
        .head(10)
        .sort_values()
    )

    st.bar_chart(top_clubes)

st.subheader("Média de controle de bola por idade")

controle_por_idade = (
    dados_filtrados.groupby("age")["ball_control"]
    .mean()
    .round(2)
    .sort_index()
)

st.line_chart(controle_por_idade)

st.info(
    "O gráfico mostra como a média de controle de bola varia "
    "entre as idades. Essa relação não significa que a idade "
    "seja a causa das diferenças observadas."
)

st.subheader("Jogadores com maior controle de bola")

top_jogadores = (
    dados_filtrados
    .sort_values("ball_control", ascending=False)
    .head(10)
)

st.dataframe(
    top_jogadores[
        ["player", "age", "country", "club", "ball_control"]
    ].reset_index(drop=True),
    hide_index=True,
    use_container_width=True
)

st.bar_chart(
    top_jogadores.set_index("player")["ball_control"]
)

st.divider()

st.caption(
    "Football Data Insights | Python, Pandas e Streamlit"
)

