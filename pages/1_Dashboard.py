import streamlit as st
import plotly.express as px

from src.data_loader import load_data
from src.preprocessing import preprocess


# Configuration de la page
st.set_page_config(
    page_title="Dashboard films",
    layout="wide"
)


# Chargement des données
@st.cache_data
def get_data():

    df = load_data("data/movies.csv")
    df = preprocess(df)

    return df


clean_df = get_data()


# Titre
st.title("Dashboard - Analyse du catalogue de films")


st.markdown(
    """
    Cette page présente une vue globale du dataset :
    statistiques principales et premières visualisations.
    """
)


# -----------------------------
# Indicateurs principaux
# -----------------------------

nb_movies = clean_df["Title"].nunique()

nb_languages = (
    clean_df["Original_Language"]
    .nunique()
)

nb_genres = (
    clean_df["Genre"]
    .str.split(",")
    .explode()
    .str.strip()
    .nunique()
)

year_min = clean_df["Release_Year"].min()
year_max = clean_df["Release_Year"].max()

average_rating = (
    clean_df["Vote_Average"]
    .mean()
)


col1, col2, col3, col4, col5 = st.columns(5)


with col1:
    st.metric(
        "Nombre de films",
        nb_movies
    )


with col2:
    st.metric(
        "Langues",
        nb_languages
    )


with col3:
    st.metric(
        "Genres",
        nb_genres
    )


with col4:
    st.metric(
        "Période",
        f"{year_min} - {year_max}"
    )


with col5:
    st.metric(
        "Note moyenne",
        round(average_rating, 2)
    )


# -----------------------------
# Evolution par année
# -----------------------------

st.subheader("Evolution du nombre de films par année")


year_count = (
    clean_df
    .groupby("Release_Year")
    .size()
    .reset_index(name="Count")
)


fig_year = px.line(
    year_count,
    x="Release_Year",
    y="Count",
    template="plotly_white"
)


st.plotly_chart(
    fig_year,
    use_container_width=True
)


# -----------------------------
# Langues principales
# -----------------------------

st.subheader("Répartition des langues principales")


language_count = (
    clean_df["Original_Language"]
    .value_counts()
    .head(5)
    .reset_index()
)

language_count.columns = [
    "Language",
    "Count"
]


other_count = (
    clean_df["Original_Language"]
    .value_counts()
    .iloc[5:]
    .sum()
)


language_count.loc[len(language_count)] = [
    "Other",
    other_count
]


fig_language = px.pie(
    language_count,
    names="Language",
    values="Count",
    hole=0.4,
    template="plotly_white"
)


st.plotly_chart(
    fig_language,
    use_container_width=True
)