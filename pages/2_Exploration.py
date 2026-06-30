import streamlit as st
import pandas as pd

from src.data_loader import load_data
from src.preprocessing import preprocess


st.set_page_config(
    page_title="Exploration",
    layout="wide"
)


@st.cache_data
def get_data():

    df = load_data("data/movies.csv")
    df = preprocess(df)

    return df


clean_df = get_data()


st.title("Exploration interactive")

st.markdown(
    """
    Cette page permet d'explorer le catalogue
    en utilisant différents filtres.
    """
)

st.sidebar.header("Filtres")


year_range = st.sidebar.slider(
    "Année de sortie",
    int(clean_df["Release_Year"].min()),
    int(clean_df["Release_Year"].max()),
    (
        int(clean_df["Release_Year"].min()),
        int(clean_df["Release_Year"].max())
    )
)


languages = st.sidebar.multiselect(
    "Langue",
    sorted(
        clean_df["Original_Language"]
        .dropna()
        .unique()
    )
)


min_rating = st.sidebar.slider(
    "Note minimale",
    0.0,
    10.0,
    0.0
)

filtered_df = clean_df[
    (clean_df["Release_Year"] >= year_range[0]) &
    (clean_df["Release_Year"] <= year_range[1]) &
    (clean_df["Vote_Average"] >= min_rating)
]


if languages:
    filtered_df = filtered_df[
        filtered_df["Original_Language"]
        .isin(languages)
    ]

st.subheader(
    f"{len(filtered_df)} films trouvés"
)


st.dataframe(
    filtered_df[
        [
            "Title",
            "Release_Year",
            "Genre",
            "Vote_Average",
            "Popularity"
        ]
    ],
    use_container_width=True
)

