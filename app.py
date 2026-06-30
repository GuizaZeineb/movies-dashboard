import streamlit as st


st.set_page_config(
    page_title="Movies Dashboard",
    layout="wide"
)


st.title(" Tableau de bord des films")

st.markdown(
    """
    ## Bienvenue

    Cette application permet d'explorer un jeu de données de films.

    Sections disponibles :

    - Vue d'ensemble du catalogue
    - Exploration interactive des données
    - Recherche et analyse d'un film
    - Visualisations avancées
    """
)