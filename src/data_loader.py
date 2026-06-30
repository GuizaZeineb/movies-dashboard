import pandas as pd
import streamlit as st


@st.cache_data
def load_data(path):

    df = pd.read_csv(
        path,
        sep=",",
        engine="python"
    )

    return df