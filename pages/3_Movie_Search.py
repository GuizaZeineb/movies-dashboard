import streamlit as st
import pandas as pd

from src.data_loader import load_data
from src.preprocessing import preprocess


st.set_page_config(
    page_title="Analyse d'un film",
    layout="wide"
)


@st.cache_data
def get_data():

    df = load_data("data/movies.csv")
    df = preprocess(df)

    return df


clean_df = get_data()


st.title("🎬 Analyse d'un film")


st.markdown(
    """
    Recherchez un film pour afficher ses informations détaillées.
    """
)


# -----------------------------
# Sélection du film
# -----------------------------

movie_title = st.selectbox(
    "Choisir un film",
    sorted(clean_df["Title"].dropna().unique())
)


movie = clean_df[
    clean_df["Title"] == movie_title
].iloc[0]


# -----------------------------
# Affichage
# -----------------------------

col1, col2 = st.columns([1, 2])


with col1:
    if pd.notna(movie["Poster_Url"]):
        st.image(movie["Poster_Url"], use_container_width=True)
    else:
        st.warning("Pas d'affiche disponible")


with col2:
    st.subheader(movie["Title"])

    st.write(f"**Année :** {movie['Release_Year']}")
    st.write(f"**Langue :** {movie['Original_Language']}")
    st.write(f"**Note moyenne :** {movie['Vote_Average']}")
    st.write(f"**Nombre de votes :** {movie['Vote_Count']}")
    st.write(f"**Popularité :** {movie['Popularity']}")

    st.write("**Genres :**")
    st.write(movie["Genre"])

    st.markdown("### Résumé")
    st.write(movie["Overview"])