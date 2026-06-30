import streamlit as st
import plotly.express as px

from src.data_loader import load_data
from src.preprocessing import preprocess


st.set_page_config(
    page_title="Analyse avancée",
    layout="wide"
)


@st.cache_data
def get_data():

    df = load_data("data/movies.csv")
    df = preprocess(df)

    return df


clean_df = get_data()


st.title("Analyse avancée")


st.markdown(
    """
    Cette page présente une analyse de la relation
    entre la popularité et la note moyenne des films.
    
    Les films ayant moins de 10 votes sont exclus afin
    d'éviter les évaluations peu représentatives.
    """
)


analysis_df = clean_df[
    clean_df["Vote_Count"] >= 10
].copy()


analysis_df["Primary_Genre"] = (
    analysis_df["Genre"]
    .str.split(",")
    .str[0]
    .str.strip()
)


threshold = analysis_df["Popularity"].quantile(0.99)


analysis_df = analysis_df[
    analysis_df["Popularity"] <= threshold
]


fig = px.scatter(
    analysis_df,
    x="Popularity",
    y="Vote_Average",
    color="Primary_Genre",
    size="Vote_Count",
    hover_name="Title",
    template="plotly_white",
    title="Popularité et note moyenne par genre"
)


fig.update_layout(
    height=650
)


st.plotly_chart(
    fig,
    use_container_width=True
)


